import matplotlib.pyplot as plt 
import numpy as np 

nL = 10
nR = 10

n = np.arange(-nL,nR+1)  
u = np.array([np.zeros((1,nL))])
u = np.append(u,np.array([np.ones((1,nR+1))]))

u1 = np.array([np.zeros((1,nL+2))])
u1 = np.append(u1,np.array([np.ones((1,nR-1))]))

u2 = np.array([np.zeros((1,nL+7))])
u2 = np.append(u2,np.array([np.ones((1,nR-6))]))

u3 = u[::-1]
u4 = np.array([np.ones((1,nL+5))])
u4 = np.append(u4,np.array([np.zeros((1,nR-4))]))

u5 = 2*(u1-u2-u3+u4)
print('u1 =',u1)
print('u2 =',u2)
print('u3 =',u3)
print('u4 =',u4)
print('x =',u5)
plt.subplot(4,1,1)
plt.stem(n,u5)
plt.title('y[n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

plt.subplot(4,1,2)
plt.stem(n,2-3*u5)
plt.title('2-3y[n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

plt.subplot(4,1,3)
ub = np.roll(u5,2)
plt.stem(n,3*ub)# % plot u[n-5]
plt.title('3y[n-2]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

plt.subplot(4,1,4)
plt.stem(n,2-2*ub)# % plot u[n-5]
plt.title('2-2y[-2+n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

plt.show()