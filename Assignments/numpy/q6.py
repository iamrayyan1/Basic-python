# 6. Generate a 2x2 matrix and calculate its determinant and inverse.

import numpy as np
arr = np.arange(1,10).reshape(2,2)
print(arr)
print("Determinant: \n", np.linalg.det(arr))
print("Inverse: \n", np.linalg.inv(arr))
