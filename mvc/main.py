import tkinter as tk
from models.model import Model
from controllers.controller import Controller
from controllers.camera import CameraController
from models.camera import CameraModel


def main():
    root = tk.Tk()
    model = Model()
    CameraController(CameraModel(), root)
    Controller(model, CameraModel(), root)
    
    root.mainloop()

if __name__ == "__main__":
    main() 
