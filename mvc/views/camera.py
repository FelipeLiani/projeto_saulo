import tkinter as tk
from PIL import Image, ImageTk

class CameraView:
    def __init__(self, root, update_callback):
        self.root = root
        self.update_callback = update_callback
        self.root.title("Webcam MVC")

        # Label para exibir a imagem da câmera
        self.label = tk.Label(self.root)
        self.label.pack(padx=10, pady=10)

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