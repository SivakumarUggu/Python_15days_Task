#Create a numpy array and reshape it into a different shape.
import numpy as np
numpy_array=np.array([3,5,7,2])
print('Original shape is:', numpy_array)
new_shape=(2,2)
reshaping=numpy_array.reshape(new_shape)
print('after reshaping:', reshaping)
