import pyaudio
import numpy
import wave
import scipy.io.wavfile as wavfile

RATE = 16384
RECORD_SECONDS = 4
CHUNKSIZE = 1024
WAVE_OUTPUT_FILENAME = "voice.wav"
CHANNELS = 1
FORMAT = pyaudio.paInt16


def record_audio():
    # initialize portaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

    frames = [] # A python-list of chunks(numpy.ndarray)
    print("Recording starting now!")
    for _ in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
        data = stream.read(CHUNKSIZE)
        frames.append(numpy.frombuffer(data, dtype=numpy.int16))

    print('Recording finished!')
    #Convert the list of numpy-arrays into a 1D array (column-wise)
    numpydata = list(numpy.hstack(frames))

    # close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    transformed = wav_to_array()

    return transformed

def wav_to_array():
    fs_rate, signal = wavfile.read("voice.wav")
    return signal.tolist()