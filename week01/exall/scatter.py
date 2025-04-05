import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


s = pd.read_csv("bla.csv")
s = s.replace('_',np.nan)

lst = s['price'].tolist()
lst1 = s['area'].tolist()
lst2 = s['bedrooms'].tolist()
lst3 = s['bathrooms'].tolist()
lst4 = s['stories'].tolist()
lst5 = s['parking'].tolist()


fig, axes = plt.subplots(2, 1, figsize=(14, 10))

axes[0].scatter(lst, lst1)
axes[0].set_title("Price house based on area")
axes[0].set_xlabel('Prices(MAD)')
axes[0].set_ylabel('Area')


axes[1].scatter(lst2, lst)
axes[1].set_title("Price house based on num of bedrooms")
axes[1].set_xlabel('Num of bedrooms')
axes[1].set_ylabel('Prices(MAD)')




for j in range(2):
    axes[j].xaxis.set_major_formatter(ticker.EngFormatter(unit=''))
    axes[j].yaxis.set_major_formatter(ticker.EngFormatter(unit=''))

plt.show()







