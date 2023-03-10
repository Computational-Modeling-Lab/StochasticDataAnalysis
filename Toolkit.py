import numpy as np

def Wiener(dt=1,X0=0,num_steps=10000, mu=0, sigma=1):
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
    
def OU(num_steps= 10000, alpha= 0.5, sigma= 0.5, X0= 0, dt=1, mu=0):
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

def AutocorrelationFunction(x, lag=20):
    '''
    x: Input Data
    lag: Time lag
    '''
    return np.array([1]+[np.corrcoef(x[:-i], x[i:])[0,1] for i in range(1, lag)])