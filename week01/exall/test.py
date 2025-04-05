import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

s = pd.read_csv("bla.csv")
s = s.replace('_',np.nan)

#plot 1:

fig, axes  = plt.subplots(1, 3, figsize=(15, 5))
sns.histplot(data=s, x="price", kde=True, ax=axes[0])
#plot 2:

sns.histplot(data=s, x="area", ax=axes[1], kde=True)
axes[0].xaxis.set_major_formatter(ticker.EngFormatter(unit=''))


s

plt.show()