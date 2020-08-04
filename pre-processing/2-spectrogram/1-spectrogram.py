import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
 
def feat_spectrogram(pathIn, pathOut, id):
    id= str(id)
    
    fs, x = wavfile.read(pathIn + id + '.wav')
    spectrogram, freqs, bins, im = plt.specgram(x, NFFT=1024, Fs=fs)
    print(id, spectrogram.shape)
    np.savetxt(pathOut + id + '.csv', spectrogram, delimiter=',')   

if __name__ == '__main__':
    import glob

    pathIn= '../data/1-308_AUDIO/chunks/' 
    pathOut= '../data/1-308_AUDIO/spectrograms/' 

    filenames= glob.glob(pathIn + '*.wav')
    for id in range( len(filenames) ):        
        feat_spectrogram(pathIn, pathOut, id)   

    print(pathOut)
    print("done")












