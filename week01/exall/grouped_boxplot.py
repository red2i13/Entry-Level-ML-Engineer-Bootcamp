import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

s = pd.read_csv("bla.csv")
s = s.replace('_',np.nan).dropna()

sns.set_style('darkgrid')
ax = sns.boxplot(x='bedrooms', y = 'price', hue='furnishingstatus', data=s)

# ax = sns.boxplot(x='area', y = 'price', hue='bedrooms', data=s)

ax.xaxis.set_major_formatter(ticker.EngFormatter(unit=''))
ax.yaxis.set_major_formatter(ticker.EngFormatter(unit=''))

plt.show()



