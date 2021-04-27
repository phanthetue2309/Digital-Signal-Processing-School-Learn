import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sps
import math
import sounddevice as sd

F = 16000
f = 1000
duration = 3 
t = np.linspace(0, duration, duration * F, False)
y = 5*np.sin(2 * np.pi * f *t )

A = [0.1, 1, 10]
x1 = y + np.random.randn(48000) * A[0]
x2 = y + np.random.randn(48000) * A[1]
x3 = y + np.random.randn(48000) * A[2]

sd.play(x1, F)
sd.wait()
sd.play(x2, F)
sd.wait()

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(t[0:100], x1[0:100])

plt.subplot(3,1,2)
plt.plot(t[0:100], x2[0:100])

plt.subplot(3,1,3)
plt.plot(t[0:100], x3[0:100])
plt.show()

M = [3, 5, 7, 9]
plt.figure(2)
min = 1000000
for i in range(len(M)):
    b = 1 / M[i] * np.array([1] * M[i])
    c = sps.lfilter(b, 1, x2)
    plt.subplot(4,1,i+1)
    plt.plot(t[0:99], c[0:99])
    h = c - y
    h = h*h
    rmse = math.sqrt(np.sum(h)/len(t))
    plt.title('M = ' + str(M[i]) + ' rmse = ' + str(rmse))

b = 1 / M[0] * np.array([1] * M[0])
c = sps.lfilter(b, 1, x2)
sd.play(c, F)
sd.wait()

plt.show()





