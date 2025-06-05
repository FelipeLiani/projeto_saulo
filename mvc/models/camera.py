import cv2

class CameraModel:
    def __init__(self):
        self.cap = None
        self.is_running = False
        self.current_frame = None

    def start_camera(self):
        if not self.is_running:
            self.cap = cv2.VideoCapture(0)
            self.is_running = self.cap.isOpened()
            return self.is_running
        return False

    def stop_camera(self):
        if self.is_running and self.cap:
            self.is_running = False
            self.cap.release()

    def get_frame(self):
        if self.is_running and self.cap:
            ret, frame = self.cap.read()
            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_fip = cv2.flip(frame_rgb, 1)
                self.current_frame = frame_fip  # Armazena o frame atual
                return frame_fip
        return None
