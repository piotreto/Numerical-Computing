import numpy as np
from copy import deepcopy

def LU(A):
    n = A.shape[0]

    for col in range(n):
        for row in range(col+1, n):
            multiplier = A[row][col] / A[col][col]
            A[row, col:] -= (A[col,col:] * multiplier)
            A[row,col] = multiplier
    return A
size = 1000
A = np.random.rand(size, size)
A1 = deepcopy(A)
A1 = LU(A1)
L = np.tril(A1)
U = np.triu(A1)
np.fill_diagonal(L,1)

print(abs(A - L @ U) < 1e-7)
print(np.allclose(A, L @ U))