from views.view import View
from models.model import Model

class Controller:
    def __init__(self, model, root):
        self.model = model
        self.view = View(root, self)
        self.monitoramento_ativo = False

    def toggle_monitoramento(self):
        self.monitoramento_ativo = not self.monitoramento_ativo

        if self.monitoramento_ativo:
            print("Controller=> Monitoramento INICIADO")
            self.view.btn_monitoramento.config(text="Parar Monitoramento")
            self.model.acessar_bd("Monitoramento iniciado")
        else:
            print("Controller=> Monitoramento PARADO")
            self.view.btn_monitoramento.config(text="Iniciar Monitoramento")
            self.model.acessar_bd("Monitoramento parado")

    def abrir_estatisticas(self):
        print("Controller=> Abrindo estatísticas...")
        self.view.criar_janela_modal("Estatísticas")

    def abrir_sugestoes(self):
        print("Controller=> Abrindo sugestões...")
        self.view.criar_janela_modal("Sugestões de Alongamento")

    def abrir_historico(self):
        print("Controller=> Abrindo histórico...")
        self.view.criar_janela_modal("Histórico de Sessões")

    def abrir_configuracoes(self):
        print("Controller=> Abrindo configurações...")
        self.view.criar_janela_modal("Configurações")
