import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plt 
import scipy.signal as sps
import math
import sounddevice as sd
# cau a
def create_sound(frequency,fs,seconds,A):
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)
    #tat do thi thi moi chay file am thanh dc
    note = 5*np.sin(frequency * t * 2 * np.pi ) + A*np.random.randn(len(t))  # Generate a 1000 Hz sine wave
    plt.plot(t[0:100],note[0:100],'tab:orange')
    plt.show()

    audio = note * (2**15 - 1) / np.max(np.abs(note))   # Ensure that highest value is in 16-bit range  
    audio = audio.astype(np.int16)  # Convert to 16-bit data
   
    play_obj = sa.play_buffer(audio, 2, 2, fs)  # Start playback
    play_obj.wait_done()   # Wait for playback to finish before exiting
    
frequency = 1000  # Our played note will be 440 Hz
fs = 16000  # 16000 samples per second
seconds = 3  # Note duration of 2 seconds

A = 0.1
create_sound(frequency,fs,seconds,A)
A = 1
create_sound(frequency,fs,seconds,A)
A = 10
create_sound(frequency,fs,seconds,A)

#cau b
t = np.linspace(0, seconds, seconds * fs, False)
x = 5*np.sin(frequency * t * 2 * np.pi ) 
M = [3, 5, 7, 9]

for i in range(len(M)):
    b = 1 / M[i] * np.array([1] * M[i])
    c = sps.lfilter(b, 1, x)
    plt.subplot(4,1,i+1)
    plt.plot(t[0:100], c[0:100],'tab:red')
    h = c - x
    v = h*h
    rmse = math.sqrt(sum(v)/len(t))
    plt.title('M = ' + str(M[i]) + ' and  RMSE = ' + str(rmse))
    
b = 1 / M[0]*np.array([1]*M[0])
c = sps.lfilter(b, 1, x)
sd.play(c, fs)
sd.wait()

plt.show()
