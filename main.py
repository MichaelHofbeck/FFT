from json.tool import main
from unittest import loader

from numpy import size
import numpy_fft
import data_generation
import generate_plots
import yaml

def main():
    data = data_generation.generate_array(dictionary['size'])
    numpy_fft.run_dft(data)
    numpy_fft.run_david_mike(data)
    numpy_fft.run_fft(data)
    generate_plots.size_time_graph(10000, 100)

if __name__ == '__main__':
    with open('config.yml', 'r') as file:
        dictionary = yaml.safe_load(file)
    main()
