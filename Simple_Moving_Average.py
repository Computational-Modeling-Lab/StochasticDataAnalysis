# Code for SMA in python
# Created By Nikos Avgoustis

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("fivethirtyeight")

# Simple moving average
def SMA(data,lag=3):
    sma = []
    for i in range(lag):
        sma.append(np.nan)
    for i in range(lag,len(data)+1):
        sma.append(np.mean(data[i-lag:i]))
    return np.array(sma)

#Create our data sets
#1. random data from a normal distribution
random_data = np.random.normal(0,1,100)
x1 = np.linspace(0,1,100) 
#2. Data from a sin function
T=1
x2 = np.linspace(0,5,200)
y = np.sin((2*np.pi/T)*x2)

# Visualize our data
plt.plot(x1,random_data)
plt.title('Random Data')

plt.plot(x2,y)
plt.title('Sinusoid data')

#Visualize results
plt.plot(random_data,label='Data')
plt.plot(SMA(random_data,lag=3),label="lag = 3")
plt.plot(SMA(random_data,lag=7),label="lag = 7")
plt.plot(SMA(random_data,lag=11),label="lag = 11")
plt.title("SMA for random data \n")
plt.legend()



lag=11
plt.plot(y)
plt.plot(SMA(y,lag=lag))
plt.title('SMA for sinusoid data with lag = {}'.format(lag))

plt.show()