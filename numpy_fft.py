import numpy as np
from matplotlib import pyplot as plt
import time
import cmath

# This runs and times the numpy fft
def run_fft(data):
    start = time.time()
    result = np.fft.fft(data)
    end = time.time()
    runtime = end - start
    print('Finished numpy FFT in ' + str(runtime) + ' seconds!')
    return result

# This returns the runtime of the NumPy FFT
def time_fft(data):
    start = time.time()
    np.fft.fft(data)
    end = time.time()
    runtime = end - start
    print('Finished numpy FFT in ' + str(runtime) + ' seconds!')
    return runtime

# This runs and times our scratch fft
def run_david_mike(data):
    cutoff = len(data)
    padded = data + [0]*( (1<<(cutoff-1).bit_length()) - cutoff)
    start = time.time()
    result = david_mike_fft(padded)
    end = time.time()
    runtime = end - start
    print('Finished scratch FFT in ' + str(runtime) + ' seconds!')
    return result

# This returns the runtime of the scratch FFT
def time_david_mike(data):
    cutoff = len(data)
    padded = data + [0]*( (1<<(cutoff-1).bit_length()) - cutoff)
    start = time.time()
    result = david_mike_fft(padded)
    end = time.time()
    runtime = end - start
    print('Finished scratch FFT in ' + str(runtime) + ' seconds!')
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
    # print(np.allclose(final, np.fft.fft(data)))
    return final

# This runs and times the Discrete Fourier Transform
def run_dft(data):
    start = time.time()
    result = dft(data)
    end = time.time()
    runtime = end - start
    print('Finished DFT in ' + str(runtime) + ' seconds!')
    return result

# This returns the runtime of the DFT
def time_dft(data):
    start = time.time()
    dft(data)
    end = time.time()
    runtime = end - start
    print('Finished DFT in ' + str(runtime) + ' seconds!')
    return runtime

# This is the implementation of the DFT from scratch
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
