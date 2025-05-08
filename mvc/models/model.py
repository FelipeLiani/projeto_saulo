class Model:
    def __init__(self):
        self.db_connection = None  # Conexão com banco de dados

    def acessar_bd(self, acao: str):
        print("Model=> Simulacao de acesso ao banco de dados: ", acao)
        return "Model=> acabei de executar uma ação no bd e estou retornando os dados 1."

