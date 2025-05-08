import tkinter as tk
from tkinter import ttk

class Interface_Grafica:
    def __init__(self, window):
        self.window = window
        self.window.title("Aqui vai o nome de sua aplicação")
        self.window.geometry("800x800")  # Aumentei a altura para acomodar os novos frames    

        self.style = ttk.Style()# Criar estilo personalizado que é utilizado nos frames top e bottom
        self.style.configure('Cinza.TFrame', background='#4F4F4F')  # Cor cinza chumbo
        self.style.configure('BrancoTexto.TLabel', background='#4F4F4F', foreground='white')  # Texto branco sobre fundo cinza

        # Frame do topo
        self.top_frame = ttk.Frame(self.window, height=50, style='Cinza.TFrame')
        self.top_frame.pack(fill="x", padx=1, pady=1)        
        self.top_frame.pack_propagate(False) # Forçar a altura do frame
        self.title_label = ttk.Label(self.top_frame,text="Aqui vai uma mensagem de título.", font=("Helvetica", 16, "bold"),style='BrancoTexto.TLabel')
        self.title_label.place(x=20, y=10)

        # Frame principal
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(padx=1, pady=1, fill="both", expand=True)
        self.botao_1 = ttk.Button(self.main_frame, text="Chama Método 1", command=self.metodo_um)  
        self.botao_1.place(x=20, y=10)

        # Frame do rodape
        self.bottom_frame = ttk.Frame(self.window, height=50, style='Cinza.TFrame') # Frame do rodapé com novo estilo
        self.bottom_frame.pack(fill="x", padx=1, pady=1, side="bottom")
        self.bottom_frame.pack_propagate(False) # Forçar a altura do frame
        self.botao_2 = ttk.Button(self.bottom_frame, text="Chama Método 2", command=self.metodo_dois)
        self.botao_2.place(x=20, y=10)
        
    def metodo_um(self):
        print("Método 1 foi chamado ao clicar no botão")

    def metodo_dois(self):
        print("Método 2 foi chamado ao clicar no botão")

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface_Grafica(root)
    root.mainloop() 
    