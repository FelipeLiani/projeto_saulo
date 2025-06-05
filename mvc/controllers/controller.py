from views.view import View
from models.model import Model
from utils.suggestion import get_response
from utils.matplot import create_graph

class Controller:
    def __init__(self, model, cameraModel, root):
        self.model = model
        self.cameraModel = cameraModel
        self.view = View(root, self)
        self.monitoramento_ativo = False

    def toggle_monitoramento(self):
        self.monitoramento_ativo = not self.monitoramento_ativo

        if self.monitoramento_ativo:
            print("Controller=> Monitoramento INICIADO")
            self.model.acessar_bd("Monitoramento iniciado")
            self.handle_action('start')
            self.view.btn_monitoramento.config(text="Parar Monitoramento")
        else:
            print("Controller=> Monitoramento PARADO")
            self.model.acessar_bd("Monitoramento parado")
            self.handle_action('stop')
            self.view.btn_monitoramento.config(text="Iniciar Monitoramento")
        
    def handle_action(self, action):
        """Processa as ações do usuário (iniciar/parar)."""
        if action == "start":
            if self.cameraModel.start_camera():
                self.monitoramento_ativo = True
                self.view.criar_janela_modal_camera('janela')
                self.update_frame()
        elif action == "stop":
            self.cameraModel.stop_camera()
            self.monitoramento_ativo = False

    def abrir_estatisticas(self):
        print("Controller=> Abrindo estatísticas...")
        window = self.view.criar_janela_com_grafico()
        create_graph(window)


    def abrir_sugestoes(self):
        response = get_response()
        print("Controller=> Abrindo sugestões...")
        self.view.criar_modal("Sugestões", response)

    def abrir_historico(self):
        print("Controller=> Abrindo histórico...")
        self.view.criar_janela_modal("Histórico de Sessões")

    def abrir_configuracoes(self):
        print("Controller=> Abrindo configurações...")
        self.view.criar_janela_modal("Configurações")
    
    def update_frame(self):
        """Atualiza o frame da câmera na interface."""
        if self.monitoramento_ativo:
            frame = self.cameraModel.get_frame()
            if frame is not None:
                self.view.update_image(frame)
            # Agenda a próxima atualização (aproximadamente 30 FPS)
            self.view.window.after(33, self.update_frame)
