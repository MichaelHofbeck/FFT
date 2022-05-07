from json.tool import main
from unittest import loader

from numpy import size
import numpy_fft
import data_generation
import yaml

def main():
    numpy_fft.run_dft(data_generation.generate_array(dictionary['size']))

if __name__ == '__main__':
    with open('config.yml', 'r') as file:
        dictionary = yaml.safe_load(file)
    main()
