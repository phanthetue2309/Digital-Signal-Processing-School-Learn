import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.ticker import MaxNLocator

nL = 10
nR = 10

n = np.arange(-nL,nR+1)  
fig, ax = plt.subplots(4)

u = np.array([0] *nL + [1]*(nR+1)) # lenh moi update 
u1 = np.array([0] *(nL + 2) + [1]*(nR-1))
u2 = np.array([0] *(nL + 7) + [1]*(nR-6))
u3 = u[::-1]
u4 = np.array([1] *(nL + 5) + [0]*(nR-4))
u5 = 2*(u1-u2-u3+u4)

print('u = ',u)
print('u1 =',u1)
print('u2 =',u2)
print('u3 =',u3)
print('u4 =',u4)
print('x =',u5)

ax[0].stem(n,u5,'tab:orange')
ax[0].set_title('y[n]')

ax[1].stem(n,2-3*u5,'tab:green')
ax[1].set_title('2-3y[n]')

ub = np.roll(u5,2)
ax[2].stem(n,3*ub,'tab:red')
ax[2].set_title('3y[n-2]')

ax[3].stem(n,2-2*ub)
ax[3].set_title('2-2y[-2+n]')

for ax1 in ax.flat:
    ax1.set(xlabel= 'Time(n)',ylabel ='Amplitude')
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()