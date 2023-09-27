import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    def __init__(self, figure):
        super().__init__()

        self.title("Stocks")
        self.Label = tk.Label(text="Market Cap", font=("Arial", 32))
        self.Label.pack()

        marketcap = FigureCanvasTkAgg(figure, master=self)
        marketcap.get_tk_widget().pack()
        


