from cProfile import label
import numpy_fft
import data_generation
import matplotlib.pyplot as plt
import numpy as np

def size_time_graph(size, interval):
    sizes, dft, fft, mikedavidfft = [], [], [], []
    for i in range(1, size, interval):
        data = data_generation.generate_array(i)
        sizes.append(i)
        dft.append(numpy_fft.run_dft(data))
        mikedavidfft.append(numpy_fft.run_david_mike(data))
        fft.append(numpy_fft.run_fft(data))
    plt.plot(sizes, dft, label = 'DFT')
    plt.plot(sizes, fft, label = 'FFT')
    plt.plot(sizes, mikedavidfft, label = 'Mike David FFT')
    # plt.yscale('log')
    plt.legend()
    plt.show()

def plot_fft(data):
    n = len(data)
    x = np.linspace(0.0, 1.0/(2.0 * n), n//2)
    plt.plot(x, 2.0/n * np.abs(data[:n//2]))
    plt.show()




