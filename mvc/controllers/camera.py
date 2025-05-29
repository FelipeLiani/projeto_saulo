from views.camera import CameraView

class CameraController:
    def __init__(self, model, root):
        self.model = model
        self.view = CameraView(root, self)
        self.is_running = False

    def handle_action(self, action):
        """Processa as ações do usuário (iniciar/parar)."""
        if action == "start":
            if self.model.start_camera():
                self.is_running = True
                self.update_frame()
            else:
                self.view.show_error("Não foi possível acessar a câmera.")
        elif action == "stop":
            self.model.stop_camera()
            self.is_running = False
            self.view.show_error("Câmera parada.")

    def update_frame(self):
        """Atualiza o frame da câmera na interface."""
        if self.is_running:
            frame = self.model.get_frame()
            if frame is not None:
                self.view.update_image(frame)
            # Agenda a próxima atualização (aproximadamente 30 FPS)
            self.view.root.after(33, self.update_frame)