import tkinter as tk
from PIL import Image, ImageTk

class CameraView:
    def __init__(self, root, update_callback):
        self.root = root
        self.update_callback = update_callback
        self.root.title("Webcam MVC")

        # Label para exibir a imagem da câmera
        self.label = None

        # Botões para iniciar/parar a câmera
        self.start_button = tk.Button(self.root, text="Iniciar Câmera", command=lambda: self.update_callback.handle_action("start"))
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.root, text="Parar Câmera", command=lambda: self.update_callback.handle_action("stop"))
        self.stop_button.pack(side=tk.LEFT, padx=5)

    def update_image(self, image):
        """Atualiza a imagem exibida no label."""

        if image is not None:
            # Converte o frame numpy para ImageTk
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            self.label.configure(image=image)
            self.label.image = image  # Mantém a referência para evitar garbage collection

    def show_error(self, message):
        """Exibe uma mensagem de erro."""
        self.label.configure(image='', text=message)

    def criar_janela_modal(self, titulo):
        janela = tk.Toplevel(self.root)
        janela.title(titulo)
        janela.geometry("800x600")
        janela.resizable(False, False)
        janela.grab_set()  # Torna a janela modal
        janela.after_cancel

        self.label = tk.Label(janela)
        self.label.pack(padx=20, pady=20)

        tk.Button(
            janela,
            text="Fechar",
            command=lambda: self.close_this_shit(janela)
        ).pack(pady=15)

    def close_this_shit(self, janela):
        self.update_callback.handle_action("stop")
        janela.destroy()