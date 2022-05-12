from cProfile import label
import numpy_fft
import data_generation
import matplotlib.pyplot as plt

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




