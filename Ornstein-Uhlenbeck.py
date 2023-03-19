import matplotlib.pyplot as plt
import numpy as np

def OU(num_steps= 1000, alpha= 0.5, sigma= 0.5, X0= 0, dt=1, mu=0):
    '''
    dt: Time step
    X0: Starting Point
    num_steps: Number of steps
    alpha: oscillation parameter
    mu: Mean of Gaussian
    sigma: STD of Gaussian
    '''
    res = np.zeros(num_steps)
    res[0] = X0
    for t in range(1,num_steps):
        res[t] = alpha*res[t-1]*dt +sigma*np.random.normal(mu,sigma)
    return res
  
  
  
  
  
plt.figure(figsize=(20,9))
plt.plot(OU())
plt.plot(OU(X0=1))
plt.plot(OU(X0=-1))
plt.plot(OU(X0=2))
plt.plot(OU(X0=-5))
plt.show()

print('Mean = {}, STD = {}'.format(np.mean(OU(X0=1)),np.std(OU(X0=1))))
