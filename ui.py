import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    corps = []
    def createMarketCapBar(self):
        figure, axis = plt.subplots(1, 1) # row, column
        plt.bar(list(range(1, len(self.corps)+1)), marketcaps, tick_label=shorts)
        
        marketcap = FigureCanvasTkAgg(figure, master=self)
        marketcap.get_tk_widget().pack()
        

    def __init__(self, corps):
        super().__init__()
        self.corps = corps

        self.title("Stocks")
        self.Label = tk.Label(text="Market Cap", font=("Arial", 32))
        self.Label.pack()

        
        


