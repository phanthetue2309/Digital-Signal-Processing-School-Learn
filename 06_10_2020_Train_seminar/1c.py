import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sps

nL = 10
nR = 10

n = np.arange(-nL,nR+1,1)  
x = np.array([0] * (nL+nR+1))
x[10] = x[11] = 1

h1 = np.array([0] * (nL+nR+1))
h1[10] = 2
h1[11] = -1
h1[12] = 3

h2 = np.array([0] * (nL+nR+1))
h2[10] = -2
h2[11] = 1

y = h1+h2
y = np.convolve(x,y,'same')
plt.stem(n,y)
plt.xticks(n)
plt.show()
