
from pydub import AudioSegment

def merge(path, files):
    filenames= [ path + file for file in files]
    audio_full= AudioSegment.from_wav(filenames[0])

    for filename in filenames[1:]:
        audio_full= audio_full + AudioSegment.from_wav(filename)

    audio_full.export(path + "full.wav", format="wav")


if __name__ == '__main__':
    import glob

    def get_files(path):
        filenames= glob.glob(path + '*.wav')
        files=[]
        for i in range( len(filenames) ):
            file= str(i) + '.wav'
            if path + file not in filenames: continue
            files.append(file)
        return files

    path= '../../data/1-308_AUDIO/segments_adjust/' 
    files= get_files(path)
    # files=['0.wav', '1.wav']

    merge(path, files)

    print("done")
