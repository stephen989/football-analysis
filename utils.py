import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

os.chdir("C:/Users/Steph/ball")

import graphing

matplotlib.use('TkAgg')

def filter(df, column, value):
	return df[df[column] == value]

pitch = [[0,105,105,0, 0], [0,0,68,68, 0]]
box = [[0, 16.5, 16.5, 0, 0], [14, 14, 54, 54, 14]]
plt.cla()
plt.plot(*pitch, color="black")
plt.plot(*box, color = "black")
plt.show()

gridx, gridy = [0, 6, 11.25, 16.5, 25, 40, 105], [0, 14, 24, 34, 44, 54, 68]
gridx, gridy = np.meshgrid(gridx, gridy)


np.sqrt(9.15**2 - 5.5**2)
np.arcsin(7.3/9.15)
