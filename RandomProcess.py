from random import random
import numpy as np
import matplotlib.pyplot as plt

def RandomProcess(start,num_of_steps):
    random_process = []
    random_process.append(start)
    random_process = np.random.normal(0,1,num_of_steps)
    return random_process
    
s=1
start = 0
num_of_steps = 1000

random_process = RandomProcess(start,num_of_steps)


plt.plot(random_process)
plt.show()

