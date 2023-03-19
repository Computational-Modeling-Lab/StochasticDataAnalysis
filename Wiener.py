import matplotlib.pyplot as plt
import numpy as np


def Wiener(dt=1,X0=0,num_steps=1000, mu=0, sigma=1):
    '''
    dt: Time step
    X0: Starting Point
    num_steps: Number of steps
    mu: Mean of Gaussian
    sigma: STD of Gaussian
    '''
    # create result array
    res = np.zeros(num_steps)
    # initialize start value
    res[0] = X0
    # calculate and store time series
    for t in range(1,num_steps):
        #         X(t+dt)=X(t)+sqrt(dt)*npr.randn(Nt)
        res[t] = res[t-1] + np.random.normal(mu,sigma)*dt

    # return time series
    return res
  
  
  
plt.figure(figsize=(20,9))
plt.plot(Wiener())
plt.plot(Wiener())
plt.plot(Wiener())
plt.show()


final = []
for i in range(100):
    y = []
    for j in range(100):
        x = Wiener()
        y.append(x[-1])
    final.append(np.mean(y))
    
plt.figure(figsize=(20,9))
plt.plot(final)
plt.show()
