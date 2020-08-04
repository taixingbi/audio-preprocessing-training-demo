import matplotlib.pyplot as plt

from scipy.io import wavfile
import numpy as np
 
path= '../data/0-300_AUDIO/chunks/11.wav' 
fs, x = wavfile.read(path)

#https://blog.csdn.net/weixin_42943114/article/details/88735799
for nfft in [256, 512, 1024, 2048]:
    spectrogram, freqs, bins, im = plt.specgram(x, NFFT=nfft, Fs=fs) 
    print(nfft, spectrogram.shape, bins)
# nfft=256   (129, 499)
# nfft=512   (257, 166)
# nfft=1024  (513, 71)
# nfft=2048  (1025, 33)

# spectrogram, freqs, bins, im = plt.specgram(x, NFFT=1024, Fs=fs) 
# print(spectrogram[0])
# print( spectrogram.shape )





# plt.savefig('test.jpg', bbox_inches='tight', dpi=300, frameon='false')















