from views.view import View
from models.model import Model
from utils.suggestion import get_response
from controllers.camera import CameraController

class Controller:
    def __init__(self, model, camera_model, root):
        """
        Inicializa o controlador principal.

        Args:
            model: Modelo principal
            camera_model: Modelo da câmera
            root: Janela principal do Tkinter
        """
        self.model = model
        self.camera_model = camera_model
        self.root = root
        self.monitoramento_ativo = False
        self.camera_controller = CameraController(camera_model, root)
        self.view = None  # Será definido pela View após a inicialização

    def toggle_monitoramento(self):
        """Alterna entre iniciar/parar o monitoramento postural"""
        if not self.monitoramento_ativo:
            self._iniciar_monitoramento()
        else:
            self._parar_monitoramento()

        # Atualiza o estado após a operação
        self.monitoramento_ativo = not self.monitoramento_ativo

    def _iniciar_monitoramento(self):
        """Lógica completa para iniciar o monitoramento"""
        print("Iniciando monitoramento postural...")

        try:
            # 1. Inicia a captura através do CameraController
            self.camera_controller.toggle_monitoramento()

            # 2. Verifica se a câmera está realmente funcionando
            if not self.camera_model.is_running:
                raise RuntimeError("Falha ao iniciar a câmera")

            # 3. Configura a interface do usuário
            self.view.criar_janela_modal_camera("Monitoramento Postural Ativo")
            self.view.btn_monitoramento.config(text="Parar Monitoramento")

            self.monitoramento_ativo = True

            # 4. Inicia o loop de atualização de frames
            self._update_frame_loop()

        except Exception as e:
            print(f"Erro ao iniciar monitoramento: {str(e)}")
            self._parar_monitoramento()
            self.monitoramento_ativo = False

    def _parar_monitoramento(self):
        """Lógica completa para parar o monitoramento"""
        print("Parando monitoramento postural...")

        # 1. Para a captura através do CameraController
        self.camera_controller.toggle_monitoramento()

        # 2. Atualiza a interface do usuário
        if hasattr(self.view, 'btn_monitoramento'):
            self.view.btn_monitoramento.config(text="Iniciar Monitoramento")

        # 3. Garante que a câmera foi liberada
        if self.camera_model.is_running:
            self.camera_model.stop_camera()

    def _update_frame_loop(self):
        """Atualiza continuamente o frame da câmera na interface."""
        if self.monitoramento_ativo:  # Remove a verificação da câmera
            frame = self.camera_model.get_frame()
            print('tenho frame!!')

            if frame is not None:
                self.view.update_image(frame)

            # Agenda a próxima atualização
            print('rodou aqui')
            self.root.after(33, self._update_frame_loop)

    # Funções para outras funcionalidades da interface
    def abrir_estatisticas(self):
        """Abre a janela de estatísticas"""
        print("Abrindo estatísticas...")
        self.view.criar_janela_modal("Estatísticas")

    def abrir_sugestoes(self):
        response = get_response()
        print("Controller=> Abrindo sugestões...")
        self.view.criar_modal("Sugestões", response)

    def abrir_historico(self):
        """Abre a janela de histórico"""
        print("Abrindo histórico...")
        self.view.criar_janela_modal("Histórico")

    def abrir_configuracoes(self):
        """Abre a janela de configurações"""
        print("Abrindo configurações...")
        self.view.criar_janela_modal("Configurações")
