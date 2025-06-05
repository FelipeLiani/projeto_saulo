import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        controller.view = self  # Referência circular

        # Configuração da janela principal
        self.root.geometry("600x600")
        self.root.title("Monitoramento Postural")
        self.root.resizable(False, False)

        # Variáveis de estado
        self.label_camera = None

        # Configuração de estilos
        self._configurar_estilos()

        # Criar a interface
        self._criar_interface()

    def _configurar_estilos(self):
        """Configura os estilos visuais"""
        self.style = ttk.Style()
        self.style.configure('Topo.TFrame', background='#2c3e50')
        self.style.configure('Topo.TLabel',
                           foreground='white',
                           background='#2c3e50',
                           font=('Arial', 14, 'bold'))
        self.style.configure('Btn.TButton',
                           font=('Arial', 10),
                           padding=10)

    def _criar_interface(self):
        """Cria todos os elementos da interface"""
        # Frame superior
        top_frame = ttk.Frame(self.root, height=70, style='Topo.TFrame')
        top_frame.pack(fill="x")
        ttk.Label(top_frame,
                 text="Monitoramento Postural",
                 style='Topo.TLabel').pack(pady=20)

        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Botão de monitoramento (PRINCIPAL)
        self.btn_monitoramento = ttk.Button(
            main_frame,
            text="Iniciar Monitoramento",
            command=self.controller.toggle_monitoramento,
            style='Btn.TButton'
        )
        self.btn_monitoramento.pack(pady=10, fill='x')

        # Outros botões
        botoes = [
            ("Estatísticas", self.controller.abrir_estatisticas),
            ("Sugestões", self.controller.abrir_sugestoes),
            ("Histórico", self.controller.abrir_historico),
            ("Configurações", self.controller.abrir_configuracoes)
        ]

        for texto, comando in botoes:
            ttk.Button(
                main_frame,
                text=texto,
                command=comando,
                style='Btn.TButton'
            ).pack(pady=5, fill='x')

        # Rodapé
        bottom_frame = ttk.Frame(self.root, height=30, style='Topo.TFrame')
        bottom_frame.pack(fill="x", side="bottom")
        ttk.Label(bottom_frame,
                 text="© 2024 Sistema de Monitoramento Postural",
                 style='Topo.TLabel').pack(pady=5)

    def criar_janela_modal_camera(self, titulo):
        """Cria janela modal para exibir a câmera"""
        self.janela_camera = tk.Toplevel(self.root)
        self.janela_camera.title(titulo)
        self.janela_camera.geometry("800x600")
        self.janela_camera.resizable(False, False)

        # Label para exibir a imagem da câmera
        self.label_camera = tk.Label(self.janela_camera)
        self.label_camera.pack(padx=20, pady=20)

        # Botão para fechar
        tk.Button(
            self.janela_camera,
            text="Fechar",
            command=self._fechar_janela_camera
        ).pack(pady=15)

        self.janela_camera.protocol("WM_DELETE_WINDOW", self._fechar_janela_camera)

    def _fechar_janela_camera(self):
        """Fecha a janela da câmera e para o monitoramento"""
        if self.controller.monitoramento_ativo:
            self.controller.toggle_monitoramento()
        self.janela_camera.destroy()

    def update_image(self, image):
        """Atualiza a imagem exibida no label da câmera"""
        if image is not None:
            print('aaaaaaaaaaa')
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            self.label_camera.configure(image=image)
            self.label_camera.image = image  # Mantém referência

    def criar_modal(self, titulo, conteudo):
        janela = tk.Toplevel(self.window)
        janela.title(titulo)
        janela.geometry("400x600")
        janela.resizable(False, False)
        janela.grab_set()  # Torna a janela modal
        
        frame = tk.Frame(janela)
        frame.pack(fill=tk.BOTH, expand=True)

        # Criar a Scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Arial", 12))
        text_widget.insert(tk.END, conteudo)
        text_widget.pack(fill=tk.BOTH, expand=True)

        # Configurar a Scrollbar para controlar o Text
        scrollbar.config(command=text_widget.yview)

        ttk.Button(
            janela,
            text="Fechar",
            command=janela.destroy
        ).pack(pady=10)

        
        janela.update_idletasks()

    def criar_janela_modal(self, titulo):
        """Cria uma janela modal genérica"""
        janela = tk.Toplevel(self.root)
        janela.title(titulo)
        janela.geometry("400x300")
        janela.resizable(False, False)

        ttk.Label(
            janela,
            text=f"Conteúdo de {titulo} será exibido aqui",
            font=('Arial', 12)
        ).pack(expand=True)

        ttk.Button(
            janela,
            text="Fechar",
            command=janela.destroy
        ).pack(pady=10)
