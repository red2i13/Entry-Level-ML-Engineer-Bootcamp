import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

s = pd.read_csv("bla.csv")
s = s.replace('_',np.nan).dropna()

sns.set_style('darkgrid')
g = sns.pairplot(s[['price', 'area', 'bathrooms', 'bedrooms', 'parking', 'stories']], diag_kind='kde', markers='o')

for ax in g.axes.flat:
    ax.xaxis.set_major_formatter(ticker.EngFormatter(unit=''))
    ax.yaxis.set_major_formatter(ticker.EngFormatter(unit=''))

plt.show()



