import numpy as np
import matplotlib.pyplot as plt

def WhiteNoise(X0=0,num_steps=1000, mu=0, sigma=1,a=1.):
    '''
    X0: Starting Point
    num_steps: Number of steps
    mu: Mean of Gaussian
    sigma: STD of Gaussian
    a: amplification parameter
    '''
    # create result array
    res = np.zeros(num_steps)
    # initialize start value
    res[0] = X0
    # calculate and store time series
    for t in range(1,num_steps):
        res[t] = a*np.random.normal(mu,sigma)

    # return time series
    return res
  
plt.figure(figsize=(20,9))
plt.title('White Noise')
plt.plot(WhiteNoise(a=2.), label='a=2')
plt.plot(WhiteNoise(a=1.), label='a=1')
plt.plot(WhiteNoise(a=0.5), label='a=0.5')
plt.legend()
plt.show()
