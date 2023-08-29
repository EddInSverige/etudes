# https://projecteuler.net/problem=1

import matplotlib.pyplot as plt
from numba import njit
import numpy as np
import time

numbers = [x for x in range(1, 100000000) if x % 3 == 0 or x % 5 == 0]
np_numbers = np.array(numbers)

def solve_normally():
    return sum(numbers)

def solve_with_numpy():
    return np.sum(np_numbers)

@njit
def solve_with_numba():
    return np.sum(np_numbers)

if __name__  == '__main__':
    # First 'solve_with_numba' includes compilation, second is with compiled function
    solve_with_numba()

    functions = []
    times = []

    for function in [solve_normally, solve_with_numpy, solve_with_numba]:
        start = time.perf_counter()
        print(function())
        end = time.perf_counter()

        print(f'{function.__name__}: = {start - end}')

        functions.append(function.__name__)
        times.append(abs(start - end))

    fix, ax = plt.subplots()

    ax.bar(functions, times, label=["Solve normally", "Solve with Numpy", "Solve with Numba"])
    ax.legend(title="Function Times")
    plt.savefig('0001.py.png', bbox_inches='tight')
