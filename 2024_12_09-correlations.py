#https://nbviewer.org/github/twiecki/financial-analysis-python-tutorial/blob/master/1.%20Pandas%20Basics.ipynb

#source bin/activate

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = yf.download(["MGK", "VGT", "VTI", "BTC-USD", "ETH-USD", "RKLB", "AAPL", "GE", "GOOG", "IBM", "KO", "MSFT", "PEP"], start="2020-01-01", end="2024-12-09")["Adj Close"]

df.to_csv("data/2024_12_09.csv")

# clean up data

multi = pd.read_csv("data/2024_12_09.csv")

rets = multi[["AAPL", "BTC-USD", "ETH-USD", "GE", "GOOG", "IBM", "KO", "MGK", "MSFT", "PEP", "RKLB", "VGT", "VTI"]].pct_change()

#plt.scatter(rets.PEP, rets.KO)
#
#plt.xlabel("Returns PEP")
#plt.ylabel("Returns KO")
#plt.show()

pd.plotting.scatter_matrix(rets, diagonal="kde", figsize=(10,10))
plt.show()

corr = rets.corr()

plt.imshow(corr, cmap="hot", interpolation="none")
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)
plt.show()


plt.scatter(rets.mean(), rets.std())
plt.xlabel('Expected returns')
plt.ylabel('Risk')
for label, x, y in zip(rets.columns, rets.mean(), rets.std()):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (20, -20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
plt.show()
