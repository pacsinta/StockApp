import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

#intl = yf.download('INTC')
#print(intl.head())

shorts = ["AAPL", "INTC", "TSLA", "MSFT", "NVDA"]

class Corp:
    market_cap = 0
    revenue = 0
    name = ""
    def __init__(self, short):
        ticker = yf.Ticker(short)
        self.market_cap = ticker.info["marketCap"]
        

corps = []
for short in shorts:
    corp = Corp(short)
    corps.append(corp)

marketcaps = []
for corp in corps:
    marketcaps.append(corp.market_cap)


# Create window
window = tk.Tk()
window.title("Stocks")


figure, axis = plt.subplots(1, 1) # row, column

plt.bar(list(range(1, len(corps)+1)), marketcaps, tick_label=shorts)

marketcap_label = tk.Label(text="Market Cap", font=("Arial", 32))
marketcap_label.pack()
marketcap = FigureCanvasTkAgg(figure, master=window)
marketcap.get_tk_widget().pack()
window.mainloop()