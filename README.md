# IoT-Botnet
import sys
import matplotlib
import numpy
import pandas as pd
import scipy
import sklearn
from matplotlib import pyplot as plot
from pandas.plotting import scatter_matrix
print('scipy: {}'.format(scipy.__version__))
print('matplotlib: {}'.format(matplotlib.__version__))
print('sys: {}'.format(sys.version))
print('numy: {}'.format(numpy.__version__))
print('pandas: {}'.format(pd.__version__))
print('sklearn: {}'.format(sklearn.__version__))
dataset = pd.read_csv( r'E:\D-drive\Project\Dataset\CSV_BoT-IoT\Entire Dataset\UNSW_2018_IoT_Botnet_Dataset_1.csv')
print(dataset.shape)
print(dataset.groupby('attack').size())
