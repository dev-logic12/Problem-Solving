import numpy as np

def solution(arr):
    matrix = np.array(arr)
    if np.array_equal(matrix, matrix.T):
        return 1
    else:
        return 0
