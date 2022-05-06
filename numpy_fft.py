import numpy as np
import time
import cmath

def run_fft(data):
    start = time.time()
    np.fft.fft(data)
    end = time.time()
    runtime = end - start
    print(runtime)

def david_mike_fft(data):
    pass
    return

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
        re_used = -2.0*n*cmath.pi/N
        for k, num in enumerate(data):
            total += cmath.exp(complex(0.0, re_used*k))*num
        transformed.append(total)
    return transformed
