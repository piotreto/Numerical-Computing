import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
from functools import partial
from time import time

def gauss_jordan_partial_pivoting(A,B):
    n = A.shape[0]

    for col in range(n):
        pivot_idx = np.argmax(np.abs(A[:,col][col:])) + col
        A[[col,pivot_idx]] = A[[pivot_idx,col]]
        B[col],B[pivot_idx] = B[pivot_idx],B[col]
        if A[col,col] == 0:
            return "Brak rozwiazan"
        for row in range(n):
            if col == row: 
                continue
            multiplier = A[row,col] / A[col,col]
            A[row,:] -= (A[col,:] * multiplier)
            B[row] -= (B[col] * multiplier)
    for row in range(n):
        B[row] = B[row] / A[row][row]

    return B


def plot_time(func, inputs):
    x, y = [], []
    for (A,B) in inputs:
        start = time()
        if(func.__name__ == 'lstsq'):
            func(A,B, rcond=None)
        else:
            func(A,B)
        finish = time()
        print(f"{func.__name__} -- {A.shape[0]} -- {finish - start}s")
        x.append(A.shape[0])
        y.append(finish - start)
    plt.errorbar(x, y, fmt='-o', label=func.__name__)

def plot_times(functions):
    sizes = [500 + i for i in range(100,1100,100)]
    for func in functions:
        inputs = [(100 * np.random.rand(size, size), 100 * np.random.rand(size)) for size in sizes]
        plot_time(func, inputs)
    plt.legend()
    plt.xlabel("Input")
    plt.ylabel("Time [s]")
    plt.show()

plot_times([gauss_jordan_partial_pivoting, np.linalg.solve, np.linalg.lstsq])


