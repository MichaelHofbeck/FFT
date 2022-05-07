from json.tool import main

from numpy import size
import numpy_fft
import data_generation
import scratch_fft
import yaml
import time

def main():
    data = data_generation.generate_array(dictionary['size_base'] ** dictionary['size_power'])
    start = time.time()
    numpyfft = numpy_fft.run_fft(data)
    end = time.time()
    print("Numpy FFT finished in " + str(end - start) + " seconds!")
    start = time.time()
    scratchfft = scratch_fft.scratch_fft(data)
    end = time.time()
    print("Scratch FFT finished in " + str(end - start) + " seconds!")

if __name__ == '__main__':
    with open('config.yml', 'r') as file:
        dictionary = yaml.safe_load(file)
    main()
