# 10. Implement a function that accepts a NumPy array and normalizes it (subtracts the mean and divides by the standard deviation). Apply this function to a sample array.

import numpy as np

def normalize(arr):
    mean = np.mean(arr)
    std_dev = np.std(arr)
    modified = (arr - mean) / std_dev
    return modified

arr = np.random.randint(1, 101, 10)
print("Array:", arr)

modified = normalize(arr)
print("Normalized Array:", modified)
