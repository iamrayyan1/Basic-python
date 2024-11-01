# 5. Create a NumPy array of 10 values and apply the square root function to each element.

import numpy as np
arr = np.random.randint(1, 101, 10)
sq_arr = np.sqrt(arr)
print("Original Array:\n", arr)
print("Square Root:\n", sq_arr)
