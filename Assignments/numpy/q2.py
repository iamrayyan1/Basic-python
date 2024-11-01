# 2. Generate a 3x3 matrix with random integers. Calculate the transpose of the matrix.

import numpy as np

matrix = np.random.randint(1,10,(3, 3))
t = np.transpose(matrix)

print("Matrix:\n")
print(matrix)
print("\nTranspose of the Matrix:\n")
print(transpose_matrix)
