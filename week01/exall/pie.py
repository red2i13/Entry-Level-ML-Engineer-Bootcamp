import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


s = pd.read_csv("bla.csv")
s = s.replace('_',np.nan).dropna()



lst = [s['mainroad'].tolist().count('yes'), s['mainroad'].tolist().count('no')]
lst1 = [s['guestroom'].tolist().count('yes'), s['guestroom'].tolist().count('no')]
lst2 = [s['hotwaterheating'].tolist().count('yes'), s['hotwaterheating'].tolist().count('no')]
lst3 = [s['airconditioning'].tolist().count('yes'), s['airconditioning'].tolist().count('no')]
lst4 = [s['prefarea'].tolist().count('yes'), s['prefarea'].tolist().count('no')]
lst5 = [s['furnishingstatus'].tolist().count('furnished'), s['furnishingstatus'].tolist().count('semi-furnished'), s['furnishingstatus'].tolist().count('unfurnished')]


fig, axes = plt.subplots(2, 3, figsize=(14, 10))

axes[0][0].pie(lst)
axes[0][0].legend(['yes', 'no'])
axes[0][0].set_title("mainroad")

axes[0][1].pie(lst1)
axes[0][1].legend(['yes', 'no'])
axes[0][1].set_title("guestroom")

axes[0][2].pie(lst2)
axes[0][2].legend(['yes', 'no'])
axes[0][2].set_title("hotwaterheating")

axes[1][0].pie(lst3)
axes[1][0].legend(['yes', 'no'])
axes[1][0].set_title("airconditioning")

axes[1][1].pie(lst4)
axes[1][1].legend(['yes', 'no'])
axes[1][1].set_title("prefarea")

axes[1][2].pie(lst5)
axes[1][2].legend(['furnished', 'semi-furnished', 'unfurnished'])
axes[1][2].set_title("furnishingstatus")

plt.show()