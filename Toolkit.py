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
        res[t] = res[t-1] + np.random.normal(mu,sigma)*dt

    # return time series
    return res
    
def OU(dt=1, X0=0, num_steps= 10000, alpha=0.5, mu=0, sigma=0.5):
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
        res[t] = alpha*res[t-1]*dt + sigma*np.random.normal(mu,sigma)
    return res

def WhiteNoise(dt=1,X0=0,num_steps=10000, mu=0, sigma=1,a=2.):
    '''
    dt: Time step
    X0: Starting Point
    num_steps: Number of steps
    mu: Mean of Gaussian
    sigma: STD of Gaussian
    a: amplification parameter (a=1 gives a Wiener Process)
    '''
    # create result array
    res = np.zeros(num_steps)
    # initialize start value
    res[0] = X0
    # calculate and store time series
    for t in range(1,num_steps):
        res[t] = res[t-1] + a*np.random.normal(mu,sigma)*dt

    # return time series
    return res

def AutocorrelationFunction(x, lag=20):
    '''
    x: Input Data
    lag: Time lag
    '''
    return np.array([1]+[np.corrcoef(x[:-i], x[i:])[0,1] for i in range(1, lag)])


def MovingAverage(timeseries,lag=3,centered=False):
    '''
        Calculates The Simple Moving Average (SMA) of a timeseries with a certain lag.
        timeseries: The timeseries data to impliment the Simple Moving Average (SMA).
        lag: The lag to use for the Simple Moving Average (SMA).
        centered: If True calculates the centered (smoothing) SMA else calculates the Predictive SMA.
    '''
    ma = np.empty(len(timeseries))
    ma[:] = np.nan
    if centered:
        for i in range(lag,len(timeseries) - lag):
            ma[i] = np.mean(timeseries[i-lag//2:i+lag//2+1])
    else:
        for i in range(lag,len(timeseries)):
             ma[i] = np.mean(timeseries[i-lag:i])
    return ma
