#11.9. Implement a program that generates a random numpy array and finds the maximum and minimum values.
import numpy as np
random_numpy_array=np.random.randint(1,10,(2,2))
print(random_numpy_array)
max_value=random_numpy_array.max()
print('max_value in an array:', max_value)
min_value=random_numpy_array.min()
print('min_value in an array:', min_value)

