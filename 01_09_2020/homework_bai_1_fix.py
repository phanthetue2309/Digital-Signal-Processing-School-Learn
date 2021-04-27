import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator

nL = 10
nR = 10

n = np.arange(-nL,nR+1)  
fig, ax = plt.subplots(4)
u = np.array([0] *nL + [0]*(nR+1)) # lenh moi update 
u[9] = u[11]= -2
u[10] = 4
u[12] = 2
u[13] = -1
print(u)

ax[0].stem(n,u)
ua = u[::-1]
ua = np.roll(ua,-1)
ax[1].stem(n,3*ua) 
ub = 2*u
ax[2].stem(n,ub-1) 
uc = -u
ax[3].stem(n,uc+2)

for ax1 in ax.flat:
    ax1.set(xlabel= 'Time(n)',ylabel ='Amplitude')
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()