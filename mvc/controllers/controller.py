from views.view import View
from models.model import Model

class Controller:
    def __init__(self, model, root):
        self.model = model
        self.view = View(root, self)


    def acao_botao_1(self):        
        print("Controller=> O clique na view chamou o controller que imprimiu essa mensagem 1. Agora vou chamar o model, dizendo que o botao 1 foi clicado!")
        self.model.acessar_bd("Botão 1 acionado")


    def acao_botao_2(self):        
        print("Controller=> O clique na view chamou o controller que imprimiu essa mensagem 2. Agora vou chamar o model, dizendo que o botao 2 foi clicado!") 
        self.model.acessar_bd("Botão 2 acionado")