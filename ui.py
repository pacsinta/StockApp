import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    corp_map = []
    def createMarketCapBar(self):
        shorts = list(self.corp_map.keys())
        marketcaps = [self.corp_map[short]["market_cap"] for short in shorts]

        figure, axis = plt.subplots(1, 1) # row, column
        plt.bar(list(range(1, len(self.corp_map)+1)), marketcaps, tick_label=shorts)
        
        marketcap = FigureCanvasTkAgg(figure, master=self)
        marketcap.get_tk_widget().pack()
        

    def __init__(self, corp_map):
        super().__init__()
        self.corp_map = corp_map

        self.title("Stocks")
        self.Label = tk.Label(text="Market Cap", font=("Arial", 32))
        self.Label.pack()

        self.createMarketCapBar()

        
        


