from random import random
import numpy as np
import matplotlib.pyplot as plt


def RandomProcess(start,s,num_of_steps):
    random_process = []
    random_process.append(start)
    for i in range(num_of_steps):
        noise = np.random.normal(0,1)
        random_process.append(random_process[-1] + s*noise)
    return random_process
    
s=1
start = 0
num_of_steps = 1000

random_process = RandomProcess(start,s,num_of_steps)


plt.plot(random_process)
plt.show()

