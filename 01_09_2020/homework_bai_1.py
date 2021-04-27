import matplotlib.pyplot as plt 
import numpy as np 

nL = 10
nR = 10

n = np.arange(-nL,nR+1)  
u = np.array([np.zeros((1,nL))])
u = np.append(u,np.array([np.zeros((1,nR+1))]))
u[9] = u[11]= -2
u[10] = 4
u[12] = 2
u[13] = -1
print(u)


plt.subplot(4,1,1)
plt.stem(n,u) 
plt.title('Unit step x[n]')
plt.xlabel('Time (n)')  
plt.ylabel('Amplitude')

ua = u[::-1]
ua = np.roll(ua,-1)
print(ua) 
ax = plt.subplot(4,1,2)
plt.stem(n,3*ua) 
plt.title('Unit step Cau A')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

ub = 2*u
print(ub) 
plt.subplot(4,1,3)
plt.stem(n,ub-1) 
plt.title('Unit step Cau B')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

uc = -u
print(uc) 
plt.subplot(4,1,4)
plt.stem(n,uc+2)
plt.title('Unit step Cau C')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')
plt.show()