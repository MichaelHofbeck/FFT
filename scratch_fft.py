import numpy as np
import cmath

# The FFT computes the transform of small subsets of the array and then combing them together
# We seperate the DFT into odd indices and even indices

def scratch_fft(data):
    n = len(data)
    if n == 1:
        return data
    w = np.e**(2*np.pi*complex(0,1)/n)
    evens, odds = [], []
    for _ in range(n):
        if _ % 2:
            evens.append(data[_])
        else:
            odds.append(data[_])
    ye = scratch_fft(evens)
    yo = scratch_fft(odds)
    y = [0] * n
    for i in range(n//2):
        y[i] = ye[i] + yo[i]*w**i
        y[i + n//2] = ye[i] - yo[i]*w**i
    return y
    
