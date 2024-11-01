# 9. Create a NumPy array with 25 values and calculate the 75th percentile.

import numpy as np
arr = np.arange(1,26)
print(arr)
print("75th percentile: ", np.percentile(arr,75))
