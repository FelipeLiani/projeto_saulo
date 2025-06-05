from utils.capture import capture_movements
import os
import threading  # Faltava o import de threading

class CameraController:
    def __init__(self, model, root):
        self.model = model
        self.is_running = False
        self.root = root  # Adicione esta linha para referenciar a janela principal

        # Define o caminho do banco de dados
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(pasta_atual, '..', '..', 'database', 'databases', 'postura.db')

    def toggle_monitoramento(self):
        """Método chamado pelo botão 'Iniciar Monitoramento' da View principal."""
        if not self.is_running:
            self._iniciar_captura()
        else:
            self._parar_captura()

    def _iniciar_captura(self):
        """Inicia a captura de movimentos."""
        if self.model.start_camera():
            self.is_running = True
            # Inicia a thread para capture_movements
            threading.Thread(
                target=lambda: capture_movements(self.db_path),
                daemon=True
            ).start()
            print("Captura de movimentos iniciada!")

    def _parar_captura(self):
        """Para a captura de movimentos."""
        if self.is_running:
            self.is_running = False
            self.model.stop_camera()
            # Adicione um tempo para a thread finalizar
            threading.Event().wait(0.5)
            print("Captura de movimentos parada.")
