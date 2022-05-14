from cProfile import label
import numpy_fft
import data_generation
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import scipy.io.wavfile as wavfile

# this function runs a simulation to time the different Fourier Transforms for a given size and interval
def size_time_graph(size, interval):
    sizes, dft, fft, mikedavidfft = [], [], [], []
    for i in range(1, size, interval):
        data = data_generation.generate_array(i)
        sizes.append(i)
        dft.append(numpy_fft.time_dft(data))
        mikedavidfft.append(numpy_fft.time_david_mike(data))
        fft.append(numpy_fft.time_fft(data))
    plt.plot(sizes, dft, label = 'DFT')
    plt.plot(sizes, fft, label = 'FFT')
    plt.xlabel('Size')
    plt.ylabel('Time (seconds)')
    plt.plot(sizes, mikedavidfft, label = 'Mike David FFT')
    plt.legend()
    plt.show()

# this function plots the FFT
def plot_fft(data):
    n = len(data)
    x = np.linspace(0.0, 1.0/(2.0 * n), n//2)
    plt.plot(x, 2.0/n * np.abs(data[:n//2]))
    plt.show()

# this function plots the spectrogram - needs to be fixed.
def plot_spectrogram(data):
    fs = len(data)
    plt.specgram(data, cmap = 'rainbow')

    plt.show()


