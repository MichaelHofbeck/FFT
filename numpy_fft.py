import numpy as np
import time


def run_fft(data):
    start = time.time()
    np.fft.fft(data)
    end = time.time()
    runtime = end - start
    print(runtime)
