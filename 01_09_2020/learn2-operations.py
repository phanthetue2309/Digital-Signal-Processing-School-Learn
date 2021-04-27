import matplotlib.pyplot as plt 
import numpy as np 
#% left & right bounds of time axis (in samples)
nL = 10
nR = 10

#% processing
n = np.arange(-nL,nR+1)   #n = -nL:nR; % create discrete-time vector
#u = [zeros(1,nL), 1, ones(1,nR)]; % generate u[n]
u = np.array([np.zeros((1,nL))])
u = np.append(u,np.array([np.ones((1,nR+1))]))
plt.subplot(4,2,1)
plt.stem(n,u); #% plot u[n]
plt.title('Unit step u[n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

#up1 = [zeros(1,nL-1), 1, ones(1,nR+1)] % generate u[n+1]
up1 = np.array([np.zeros((1,nL-1))])
up1 = np.append(up1,np.array([np.ones((1,nR+2))]))
plt.subplot(4,2,2)
plt.stem(n,up1) # % plot u[n+1]
plt.title('Shifted unit step u[n+1]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

#um5 = [zeros(1,nL+5), 1, ones(1,nR-5)]; % generate u[n-5]
um5 = np.array([np.zeros((1,nL+5))])
um5 = np.append(um5,np.array([np.ones((1,nR-4))]))
plt.subplot(4,2,3)
plt.stem(n,um5)# % plot u[n-5]
plt.title('Shifted unit step u[n-5]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

x3 = n # % generate x3[n]=n
plt.subplot(4,2,4)
plt.stem(n,x3)# % plot x3[n]
plt.title('Signal x3[n]=n')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

#u2m = [ones(1,nL+2), 1, zeros(1,nR-2)]; % generate u[2-n]
u2m = np.array([np.zeros((1,nL+2))])
u2m = np.append(u2m,np.array([np.ones((1,nR-1))]))
plt.subplot(4,2,5)
plt.stem(n,u2m)# % plot u[2-n]
plt.title('Shifted & reversed unit step u[2-n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

x1 = up1-um5# % generate x1[n]
plt.subplot(4,2,6)
plt.stem(n,u2m)# % plot x1[n]
plt.title('x1[n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

#x2 = x3.*u2m; % generate x2[n]
x2 = x3*u2m
plt.subplot(4,2,7)
plt.stem(n,u2m)# % plot x2[n]
plt.title('x2[n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

#x = x1.*x2; % generate x[n]=x1[n]*x2[n]
x = x1 * x2
plt.subplot(4,2,8)
plt.stem(n,x) # % plot x[n]
plt.title('x[n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')

plt.show()
