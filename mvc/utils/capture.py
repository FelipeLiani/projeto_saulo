import os
import sqlite3
import cv2
import mediapipe as mp
from datetime import datetime

def capture_movements(db_path: str, max_duration_seconds: int = None):
    """
    Abre a câmera, inicia uma sessão no banco e, frame a frame, verifica a postura do usuário.
    Para cada frame, insere um evento em 'eventos_postura' com tipo 'correta' ou 'incorreta'.

    Parâmetros:
        db_path (str): caminho completo para o arquivo postura.db (por ex: '../databases/postura.db').
        max_duration_seconds (int, opcional): se fornecido, encerra a sessão após N segundos.
    """

    # --- 1) Conecta ao banco e cria uma nova sessão ---
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insere uma nova sessão (com início marcado agora) e obtém o id gerado
    inicio_str = datetime.now().isoformat()
    cursor.execute("INSERT INTO sessoes (inicio) VALUES (?)", (inicio_str,))
    id_sessao = cursor.lastrowid
    conn.commit()

    print(f"[MovementCapture] Sessão {id_sessao} iniciada em {inicio_str}")

    # --- 2) Configura MediaPipe Pose ---
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(
        static_image_mode=False,
        model_complexity=1,
        enable_segmentation=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    mp_drawing = mp.solutions.drawing_utils

    # --- 3) Inicia captura de vídeo (câmera 0) ---
    t0 = datetime.now()
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Não foi possível abrir a câmera.")

    t0 = datetime.now()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Converte para RGB (necessário para o MediaPipe)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)

            # Se detectou pose, analisa inclinação dos ombros
            tipo_evento = None
            if results.pose_landmarks:
                lm = results.pose_landmarks.landmark

                # Pega os pontos dos ombros
                left_shoulder = lm[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
                right_shoulder = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]

                # Calcula a diferença de Y normalizada
                dy = (left_shoulder.y - right_shoulder.y)
                dx = (left_shoulder.x - right_shoulder.x)
                slope = dy / (dx + 1e-6)  # evitar divisão por zero

                # Critério simples para determinar postura
                LIMIAR_INCLINACAO = 0.1
                if abs(slope) > LIMIAR_INCLINACAO:
                    tipo_evento = 'incorreta'
                else:
                    tipo_evento = 'correta'

            # --- 4) Insere no banco, se detectou um tipo válido ---
            if tipo_evento is not None:
                timestamp_str = datetime.now().isoformat()
                cursor.execute(
                    "INSERT INTO eventos_postura (id_sessao, timestamp, tipo) VALUES (?, ?, ?)",
                    (id_sessao, timestamp_str, tipo_evento)
                )
                conn.commit()

            # Encerra o loop se exceder max_duration_seconds
            if max_duration_seconds is not None:
                elapsed = (datetime.now() - t0).total_seconds()
                if elapsed >= max_duration_seconds:
                    print(f"[MovementCapture] Tempo máximo de {max_duration_seconds}s atingido.")
                    break

    finally:
        # --- 5) Finaliza captura e atualiza o campo 'fim' da sessão ---
        cap.release()
        cv2.destroyAllWindows()

        fim_str = datetime.now().isoformat()
        cursor.execute(
            "UPDATE sessoes SET fim = ? WHERE id = ?",
            (fim_str, id_sessao)
        )
        conn.commit()
        conn.close()

        print(f"[MovementCapture] Sessão {id_sessao} finalizada em {fim_str}")
