import matplotlib.pyplot as plt
import numpy as np
plt.style.use("fivethirtyeight")
plt.rcParams["figure.figsize"] = (20,8)
from statsmodels.tsa.stattools import acf

s1 = 1
s2 = 0.5
s3 = 0.01
number_of_steps = 100
start = 0
process1= []
process08= []
process01= []
noises = []

process1.append(start)
process08.append(start)
process01.append(start)
noises.append(start)

for i in range(number_of_steps):
    noise = np.random.normal(0,1)
    noises.append(noise)
    process1.append(s1*process1[-1] + noise)
    process08.append(s2*process08[-1] + noise)
    process01.append(s3*process01[-1] + noise)

plt.plot(process1,label="a = {}".format(s1))
plt.plot(process08,label="a = {}".format(s2))
plt.plot(process01,label="a = {}".format(s3))
plt.plot(noises,label="Noise")
plt.legend()
plt.xlabel('Steps')
plt.ylabel('Values')

plt.plot(acf(noises,adjusted=True,nlags=500))
plt.plot(acf(process01,adjusted=True,nlags=500))

plt.show()
