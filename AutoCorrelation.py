# Code for Autocorrelation in python
# Created By Nikos Avgoustis

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import acf
plt.style.use("fivethirtyeight")


#Create our data sets

#1. random data from a gaussian distribution
random_data = np.random.normal(0,1,1000)
x1 = np.linspace(0,1,1000) 

#2. Data from a sin function

x2 = np.linspace(-2*np.pi,20*np.pi,1000)
y = np.sin(x2)

# Visualize our data

plt.plot(x1,random_data)
plt.title('Random Data')

plt.show()

plt.plot(x2,y)
plt.title('Sinusoid data')

plt.show()

# Calculate and plot full Autocorrelation of both datasets
plt.plot(acf(y,adjusted=True,nlags=500))
plt.title('AutoCorrelation of Sin(x) Data')


plt.show()
