import pandas as pd


import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np


d = pd.read_csv('report.csv', index_col=0)#df.plot(x=df.index, y=df.columns)
d['5 seconds'] = (d['time']/(int(sys.argv[2])*100)).astype(int)
d = d.groupby('5 seconds').agg({'car':np.sum,'truck':np.sum,'bus':np.sum,"time":lambda x: x.iloc[0]})
d['time'] = (d['time']/100).astype(int)
d['time'] = pd.to_datetime(d['time'],unit='s')
d = d.set_index(['time'], drop=True)
d.plot()
plt.show()
