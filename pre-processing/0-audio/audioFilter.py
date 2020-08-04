from pydub import AudioSegment as am

from scipy.io import wavfile
import scipy.signal as sps

class audio:

    def __init__(self, path):
        print("audio..")
        self.path= path

    def check(self, fileIn):   
        print(self.path + fileIn)
 
        sampling_rate, data = wavfile.read(self.path + fileIn)
        print("sampling_rate:  ",sampling_rate)

        sound = am.from_file(self.path+fileIn, format="wav")
        samples = sound.get_array_of_samples()
        print("channels: ", sound.channels )

    def filter(self, fileIn, sample_rate= 16000, channel= 1):
        print(self.path + fileIn)

        audio = am.from_file(self.path + fileIn)

        audio = audio.set_frame_rate(sample_rate)
        # set channel 0 or 1?
        audio = audio.set_channels(channel)
        print("channel", channel)
        print("sample_rate", sample_rate)

        parts= fileIn.split('/')
        fileOut= parts[-1].split('.')[0] + '.wav'
        print(self.path + fileOut)
        audio.export(self.path + fileOut, format='wav')
        

if __name__ == "__main__":

    path= '../../data/1-308_AUDIO/' 

    fileIn= "308_AUDIO.wav"

    audio(path).check(fileIn)

    print("done")









