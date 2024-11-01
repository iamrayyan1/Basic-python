# 7. Create a NumPy array with 50 random values. Find the indices of the maximum and minimum values in the array.

import numpy as np
arr = np.random.randint(1, 100, 50)
print(arr)
print("Index of Maximum Value:", np.argmax(arr))
print("Index of Minimum Value:", np.argmin(arr))
