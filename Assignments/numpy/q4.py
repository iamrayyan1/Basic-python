# 4. Perform element-wise addition, subtraction, multiplication, and division on two NumPy arrays of your choice.

import numpy as np

array1 = np.random.randint(1, 11, 6)
array2 = np.random.randint(1, 11, 6)
print("Array 1:", array1)
print("Array 2:", array2)

addition = array1 + array2
print("Addition:", addition)

subtraction = array1 - array2
print("Subtraction:", subtraction)

multiplication = array1 * array2
print("Multiplication:", multiplication)

division = array1 / array2
print("Division:", division)
