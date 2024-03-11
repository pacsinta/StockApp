import yfinance as yf
import matplotlib.pyplot as plt
from ui import *


#intl = yf.download('INTC')
#print(intl.head())

shorts = ["AAPL", "INTC", "TSLA", "MSFT", "NVDA", "AMD"]

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


if __name__ == "__main__":
    app = App(figure)
    app.mainloop()