import yfinance as yf
import matplotlib.pyplot as plt
from ui import *

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

corp_map = {short: {"corp": corp, "market_cap": corp.market_cap} for short, corp in zip(shorts, corps)}

if __name__ == "__main__":
    app = App(corp_map)
    app.mainloop()