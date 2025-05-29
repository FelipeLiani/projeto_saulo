class Model:
    def __init__(self):
        self.db_connection = None  # Conexão com banco de dados

    def acessar_bd(self, acao: str):
        print(f"Model=> Simulacao de acesso ao banco de dados: {acao}")
        return f"Model=> Ação executada: {acao}"
