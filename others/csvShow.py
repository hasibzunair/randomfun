import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

#headers = ["time", "number_of_cars"]  #use if no headers
#data = pd.read_csv("report.csv", names=headers)


data = pd.read_csv("test.csv")
data.set_index("distance", inplace= True)
data.head()

data.plot()
plt.show()