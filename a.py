import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
if ret:
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    print("MediaPipe funcionando!" if results.pose_landmarks else "Nenhuma pessoa detectada")
cap.release()