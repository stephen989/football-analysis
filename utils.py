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

