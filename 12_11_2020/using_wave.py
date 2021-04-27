from scipy.io import wavfile
import matplotlib.pyplot as plt 
import numpy as np

samplerate, data = wavfile.read('Audio/lab_female.wav')
times = np.arange(len(data))/float(samplerate)
dt = 1/samplerate

frames = (float)((len(data) / samplerate))
fig, ax = plt.subplots(3)
ax[0].set_title("Tín hiệu Lab Male")
ax[0].set_xlabel('time')
ax[0].set_ylabel('amplitude') 
ax[0].plot(times,data)

print(np.amax(data))
n = 0 

data1 = data / np.max(data)
#data = data / np.amax(data)
print(np.max(data1))
r = np.correlate(data1, data1, mode='full')[len(data)-1:] 
ax[1].plot(r[0:300])

ax[2].acorr(data1,usevlines = True, normed = True, maxlags = 80, lw = 3)
#ax[2].plot(r)
plt.show()