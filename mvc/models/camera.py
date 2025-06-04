import cv2

class CameraModel:
    def __init__(self):
        self.cap = None
        self.is_running = False

    def start_camera(self):
        """Inicia a captura de vídeo da câmera padrão."""
        if not self.is_running:
            self.cap = cv2.VideoCapture(0)
            self.is_running = self.cap.isOpened()
            return self.is_running
        return False

    def stop_camera(self):
        """Para a captura de vídeo e libera a câmera."""
        if self.is_running and self.cap:
            self.is_running = False
            self.cap.release()

    def get_frame(self):
        """Captura um frame da câmera."""
        if self.is_running and self.cap:
            ret, frame = self.cap.read()
            if ret:
                # Converte o frame de BGR (OpenCV) para RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_fip = cv2.flip(frame_rgb, 1)
                return frame_fip
        return None
