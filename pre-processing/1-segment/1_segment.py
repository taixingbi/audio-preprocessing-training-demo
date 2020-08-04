
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
import scipy.io.wavfile as wavfile
import numpy as np

def segment(path, name):
    Fs, x= aIO.read_audio_file( path + name )

    segments = aS.silence_removal(x, Fs, 0.020, 0.020, smooth_window = 1.0, weight = 0.3, plot = False)
    print(segments)

    X= x[0:0]
    for i, segment in enumerate(segments):  
        print(i)
        t0= int(Fs * segment[0])
        t1= int(Fs * segment[1])
        wavfile.write( path + 'segments/' + str(i)  + '.wav', Fs, x[t0:t1])
        X= np.concatenate( (X, x[t0:t1]),  axis=0)

    wavfile.write( path + 'segments/full.wav', Fs, X )


if __name__ == '__main__':
    # path= '../data/0-300_AUDIO/' 
    # name= '300_AUDIO.wav'

    path= '../../data/1-308_AUDIO/' 
    name= '308_AUDIO.wav'
    segment(path, name)   





    print("done")
