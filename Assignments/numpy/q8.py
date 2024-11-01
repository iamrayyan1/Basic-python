# 8. Create a 3x3 matrix representing a system of linear equations. Use NumPy to solve the system and print the solution.

import numpy as np

A = np.array([[3, 2, -1],
              [2, 3, 2],
              [1, -1, 2]])
B = np.array([1, 12, 5])
print("A:\n", A)
print("B:\n", B)

ans = np.linalg.solve(A, B)
print("Answer:", ans)
