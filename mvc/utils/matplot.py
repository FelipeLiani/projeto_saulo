from utils.suggestion import fetch_data_as_json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_graph(window):
    data = fetch_data_as_json('eventos_postura', True)
    fig = Figure(figsize=(6, 4), dpi=100)

    count_correta = sum(1 for item in data if item["tipo"] == "correta")
    count_incorreta = sum(1 for item in data if item["tipo"] == "incorreta")

    ax = fig.add_subplot(111)
    ax.bar(['Correta', 'Incorreta'], [count_correta, count_incorreta], color=['#2ecc71', '#e74c3c'])

    ax.set_title('Quantidade de Posturas')
    ax.set_ylabel('Quantidade')

    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
