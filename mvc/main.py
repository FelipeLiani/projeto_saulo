import tkinter as tk
from models.model import Model
from models.camera import CameraModel
from controllers.controller import Controller
from views.view import View

def main():
    root = tk.Tk()

    # Inicializa os modelos
    main_model = Model()
    camera_model = CameraModel()

    # Cria o controlador principal
    controller = Controller(main_model, camera_model, root)

    # Cria a view principal
    view = View(root, controller)

    root.mainloop()

if __name__ == "__main__":
    main()
