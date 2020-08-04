from pydub import AudioSegment

def chunk(path_in, path_out):
    audio_full= AudioSegment.from_wav(path_in + 'full.wav')
    ms= len(audio_full)
    N= int(ms/4000)

    for i in range(N):
        st= i*4000
        ed= (i+1)*4000
        audio_full[st:ed].export(path_out + str(i) + ".wav", format="wav")

if __name__ == '__main__':
    path_in= '../../data/0-300_AUDIO/segments_adjust/' 
    path_out= '../../data/0-300_AUDIO/chunks/' 
    chunk(path_in, path_out)

    print("done")