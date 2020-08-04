import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
from PIL import Image
import numpy as np


path= '../data/0-300_AUDIO/chunks/0.wav' 

fs, s = wavfile.read(path)
print(fs)
for nfft in [256, 512, 1024, 2048]:
    frequencies, times, spectrogram = signal.spectrogram(s, fs, nfft=nfft) 
    print(nfft, spectrogram.shape)

# nfft=256   (129, 285)
# nfft=512   (257, 285)
# nfft=1024  (513, 285)
# nfft=2048  (1025, 285)


# frequencies, times, spectrogram = signal.spectrogram(s, fs, nfft=2048)  # 256 512 1024 2048
# print( spectrogram[0] ) # 285
# print( spectrogram.shape )



# print( spectrogram.max() )
# print( spectrogram.min() )


# print(frequencies)
# print(times)
# print(spectrogram.shape)


rescaled = ( 255.0 * (spectrogram - spectrogram.min()) / spectrogram.max()  ).astype(np.uint8)


# [5.63716984e+00 5.28117228e+00 1.45786309e+00 3.82687245e-03...]

# plt.pcolormesh(times, frequencies, rescaled)
# plt.imshow(spectrogram)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()

# print("done")