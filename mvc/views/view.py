import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, root, controller):
        self.window = root
        self.controller = controller
        self.window.geometry("600x600")
        self.window.title("Aplicação de Monitoramento Postural")
        self.window.resizable(False, False)

        # Configuração de estilos
        self.style = ttk.Style()
        self.style.configure('Topo.TFrame', background='#2c3e50')
        self.style.configure('Topo.TLabel', foreground='white', background='#2c3e50', font=('Arial', 14, 'bold'))
        self.style.configure('Btn.TButton', font=('Arial', 10), padding=10)

        # Criar frames
        self._criar_frame_topo()
        self._criar_frame_principal()
        self._criar_frame_rodape()

    def _criar_frame_topo(self):
        self.top_frame = ttk.Frame(self.window, height=70, style='Topo.TFrame')
        self.top_frame.pack(fill="x", padx=0, pady=0)
        self.top_frame.pack_propagate(False)

        self.title_label = ttk.Label(
            self.top_frame,
            text="Monitoramento Postural",
            style='Topo.TLabel'
        )
        self.title_label.pack(pady=20)

    def _criar_frame_principal(self):
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Botão de toggle para monitoramento
        self.btn_monitoramento = ttk.Button(
            self.main_frame,
            text="Iniciar Monitoramento",
            command=self.controller.toggle_monitoramento,
            style='Btn.TButton'
        )
        self.btn_monitoramento.pack(pady=10, fill='x')

        # Botão para estatísticas
        ttk.Button(
            self.main_frame,
            text="Ver Estatísticas",
            command=self.controller.abrir_estatisticas,
            style='Btn.TButton'
        ).pack(pady=10, fill='x')

        # Botão para sugestões
        ttk.Button(
            self.main_frame,
            text="Sugestões de Alongamento",
            command=self.controller.abrir_sugestoes,
            style='Btn.TButton'
        ).pack(pady=10, fill='x')

        # Botão para histórico
        ttk.Button(
            self.main_frame,
            text="Histórico de Sessões",
            command=self.controller.abrir_historico,
            style='Btn.TButton'
        ).pack(pady=10, fill='x')

        # Botão para configurações
        ttk.Button(
            self.main_frame,
            text="Configurações",
            command=self.controller.abrir_configuracoes,
            style='Btn.TButton'
        ).pack(pady=10, fill='x')

    def _criar_frame_rodape(self):
        self.bottom_frame = ttk.Frame(self.window, height=30, style='Topo.TFrame')
        self.bottom_frame.pack(fill="x", side="bottom")
        self.bottom_frame.pack_propagate(False)

        ttk.Label(
            self.bottom_frame,
            text="© 2023 Sistema de Monitoramento Postural",
            style='Topo.TLabel'
        ).pack(pady=5)

    def criar_janela_modal(self, titulo):
        janela = tk.Toplevel(self.window)
        janela.title(titulo)
        janela.geometry("400x300")
        janela.resizable(False, False)
        janela.grab_set()  # Torna a janela modal

        ttk.Label(
            janela,
            text=f"Conteúdo da tela de {titulo} será exibido aqui",
            font=('Arial', 12),
            justify='center'
        ).pack(expand=True, padx=20, pady=20)

        ttk.Button(
            janela,
            text="Fechar",
            command=janela.destroy
        ).pack(pady=10)
