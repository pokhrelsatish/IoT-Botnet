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
ds = pd.read_csv( r'E:\D-drive\Project\Dataset\CSV_BoT-IoT\Entire Dataset\UNSW_2018_IoT_Botnet_Dataset_1.csv')
print(ds.shape)
print(ds.groupby('attack').size())
ds.isnull().sum
ds.drop('stime', axis = 1, inplace = True)
ds.drop('flgs', axis = 1, inplace = True)
print(ds.head(5))
print(ds.describe())
print(ds.info())
print(ds.tail(5))
print(ds[5:10])
print(ds[['attack','pkts','rate','srate','drate']].head(5))
ds.plot(x= 'attack', y = 'pkts')