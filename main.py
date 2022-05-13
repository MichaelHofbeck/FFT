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
    data = data_generation.generate_array(dictionary['size'])
    generate_plots.plot_fft(numpy_fft.run_david_mike(data))
    # generate_plots.size_time_graph(10000, 100)
    # data = audio.record_audio()
    yo = audio.wav_to_array()
    generate_plots.plot_fft(numpy_fft.run_david_mike(yo))


if __name__ == '__main__':
    with open('config.yml', 'r') as file:
        dictionary = yaml.safe_load(file)
    main()
