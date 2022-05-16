from json.tool import main
from unittest import loader

from numpy import size
import numpy_fft
import data_generation
import generate_plots
import yaml
import numpy as np
import audio

def main():
    # audio_recording = audio.record_audio()
    # audio_recording = audio.wav_to_array()
    # print(len(audio_recording))
    # generate_plots.plot_fft(numpy_fft.run_david_mike(audio_recording))
    # generate_plots.plot_fft(numpy_fft.run_fft(audio_recording))
    # generate_plots.plot_spectrogram(audio_recording)
    # data = data_generation.generate_array(dictionary['size'])
    # generate_plots.plot_fft(numpy_fft.run_david_mike(data))
    generate_plots.size_time_graph(10000, 200)

if __name__ == '__main__':
    with open('config.yml', 'r') as file:
        dictionary = yaml.safe_load(file)
    main()
