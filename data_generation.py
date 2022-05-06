from random import randint


# This file creates a random array to run a fft on

def generate_array(size):
    data = [0 for _ in range(size)]
    for i in range(size):
        data[i] = randint(-100, 100)
    return data