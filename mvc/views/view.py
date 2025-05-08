import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, root, controller):
        self.window = root
        self.controller = controller
        self.window.geometry("800x800")
        self.window.title("Aqui vai o nome de sua aplicação")

        # Configuração de estilos
        self.style = ttk.Style()
        self.style.configure('Cinza.TFrame', background='#4F4F4F')
        self.style.configure('BrancoTexto.TLabel', background='#4F4F4F', foreground='white')

        # Criar frames
        self._criar_frame_topo()
        self._criar_frame_principal()
        self._criar_frame_rodape()

    def _criar_frame_topo(self):
        self.top_frame = ttk.Frame(self.window, height=50, style='Cinza.TFrame')
        self.top_frame.pack(fill="x", padx=1, pady=1)
        self.top_frame.pack_propagate(False)
        
        # Configurar título diretamente
        self.title_label = ttk.Label(self.top_frame,text="Aqui vai uma mensagem de título.",font=("Helvetica", 16, "bold"),style='BrancoTexto.TLabel')
        self.title_label.place(x=20, y=10)

    def _criar_frame_principal(self):
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(padx=1, pady=1, fill="both", expand=True)
        
        self.botao_1 = ttk.Button(self.main_frame, text="Chama Método 1", command=self.controller.acao_botao_1)
        self.botao_1.place(x=20, y=10)

        self.caixa_texto = ttk.Label(self.main_frame, text="...")
        self.caixa_texto.place(x=20, y=50)

    def _criar_frame_rodape(self):

        self.bottom_frame = ttk.Frame(self.window, height=50, style='Cinza.TFrame')
        self.bottom_frame.pack(fill="x", padx=1, pady=1, side="bottom")
        self.bottom_frame.pack_propagate(False)
        
        self.botao_2 = ttk.Button(self.bottom_frame, text="Chama Método 2", command=self.controller.acao_botao_2) 
        self.botao_2.place(x=20, y=10) 


        