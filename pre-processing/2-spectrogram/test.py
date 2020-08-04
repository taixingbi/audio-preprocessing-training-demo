import matplotlib.pyplot as plt  
import numpy as np  
  
  
np.random.seed(9360801)  
    
dt = 0.0005
t = np.arange(0.0, 20.0, dt)  
s1 = np.sin(4 * np.pi * 100 * t)  
s2 = 1.5 * np.sin(1.5 * np.pi * 400 * t)  
    
s2[t <= 10] = s2[12 <= t] = 0
    
nse = 0.2 * np.random.random(size = len(t))  
    
x = s1 + s2 + nse    
NFFT = 512 
fs = int(1.0 / dt)   
  
spectrogram, freqs, bins, im = plt.specgram(x, NFFT=1024, Fs=fs) 
print(spectrogram.shape)

# plt.specgram(x, Fs = Fs, cmap = plt.cm.bone)  
# plt.title('matplotlib.pyplot.specgram() Example\n', 
#           fontsize = 14, fontweight ='bold') 
  
# plt.show() 