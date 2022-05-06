import numpy as np
from matplotlib import pyplot as plt
import time
import cmath

def run_fft(data):
    start = time.time()
    np.fft.fft(data)
    end = time.time()
    runtime = end - start
    print(runtime)

def run_david_mike(data):
    start = time.time()
    david_mike_fft(data)
    end = time.time()
    runtime = end - start
    print('Finished in ' + str(runtime) + ' seconds!')
    return runtime

# This only works for data with length 
# power of 2 (16, 2048, 4096, etc.)
def david_mike_fft(data):
    N = len(data)
    if N <= 1: return data
    even = david_mike_fft(data[0::2])
    odd =  david_mike_fft(data[1::2])
    transformed = [cmath.exp(-2j*cmath.pi/N*k)*odd[k] for k in range(N//2)]
    final = [even[k] + transformed[k] for k in range(N//2)] + [even[k] - transformed[k] for k in range(N//2)]
    return final

def run_dft(data):
    start = time.time()
    dft(data)
    end = time.time()
    runtime = end - start
    print('Finished in ' + str(runtime) + ' seconds!')
    return runtime

def dft(data):
    N = len(data)
    transformed = []
    for n in range(N):
        total = 0
        re_used = -2j*n*cmath.pi/N
        for k, num in enumerate(data):
            total += cmath.exp(re_used*k)*num
        transformed.append(total)
    
    # This checks that the FT was computed correctly :)
    # print(np.allclose(transformed, np.fft.fft(data)))
    
    return transformed

def show_data(data):
    plt.plot(data)
    plt.show()
    return 0
