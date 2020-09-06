import matplotlib.pyplot as plt 
import numpy as np 
  
nL = 10
nR = 10
n = np.arange(-nL,nR+1)  #n = -nL:nR; 
#u = [zeros(1,nL), 1, ones(1,nR)]; % generate u[n]
u = np.array([np.zeros((1,nL))])
u = np.append(u,np.array([np.ones((1,nR+1))]))
print(u)
plt.subplot(3,1,1)
plt.stem(n,u) 
plt.title('Unit step u[n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

#u4 = [zeros(1,nL+4), 1, ones(1,nR-4)];
u4 = np.array([np.zeros((1,nL+4))])
u4 = np.append(u4,np.array([np.ones((1,nR-3))]))
plt.subplot(3,1,2)
plt.stem(n,u4); # plot u[n-4]
plt.title('Time-shifted Unit step u[n-4]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

x = u - u4;#   % generate u[n-4]
plt.subplot(3,1,3)
plt.stem(n,x); #% plot x[n]
plt.title('Signal x[n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')
plt.show()
