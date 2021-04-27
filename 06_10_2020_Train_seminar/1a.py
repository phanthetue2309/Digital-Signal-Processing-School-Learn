import numpy as np
import matplotlib.pyplot as plt
nL = 10
nR = 10

n = np.arange(-nL,nR+1,1)  
h1 = np.array([0] * (nL+nR+1))

plt.figure(1)
plt.subplot(2,1,1)
h1[10] = 2
h1[11] = -1
h1[12] = 3
plt.stem(n,h1)
plt.xticks(n)   

plt.subplot(2,1,2)
h2 = np.array([0] * (nL+nR+1))
h2[10] = -2
h2[11] = 1
plt.stem(n,h2)
plt.xticks(n)   
plt.show()
