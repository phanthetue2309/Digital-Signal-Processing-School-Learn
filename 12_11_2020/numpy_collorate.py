import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display

x, sr = librosa.load('Audio/lab_male.wav')
ipd.Audio(x, rate=sr)
librosa.display.waveplot(x, sr)
plt.show()

print(x) 

plt.acorr(x,usevlines = True, normed = True, maxlags = 80, lw = 3) 
plt.show()

#  autocorrelation produces a symmetric signal, we only care about the "right half".
r = numpy.correlate(x, x, mode='full')[len(x)-1:] 
print(x.shape, r.shape)
plt.figure(figsize=(12, 5))
#plt.plot(r[:10000]) # lấy 10000 là lấy 1 phân đoạn tương tự librosa 
plt.plot(r[:300])
plt.xlabel('Lag (samples)')
#plt.xlim(0, 10000)
plt.show()


#librosa.autocorrelate
r = librosa.autocorrelate(x, max_size=10000)  
print(r.shape)
plt.figure(figsize=(12, 5))
plt.plot(r[0:300])
#plt.plot(r)
plt.xlabel('Lag (samples)')
#plt.xlim(0, 10000)
plt.show()