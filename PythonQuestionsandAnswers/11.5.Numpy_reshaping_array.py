#Implement a program that generates a numpy array with numbers from 0 to 9 and reshapes it into a 3*3 matrix.
import numpy as np
numpy_array=np.arange(0,9)
print(f'array is:', numpy_array)
reshaping=numpy_array.reshape(3,3)
print(f'after reshaping:', reshaping)