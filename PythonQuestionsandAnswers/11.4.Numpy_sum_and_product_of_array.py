#11.4.Given a list of numbers create a numpy array and find the sum and product of its elements.
import numpy as np
#1D array product
numpy_array=np.array([3,4,5])
OneD_product=numpy_array.prod()
print('1D array product is:', OneD_product)

#2D array product
numpy_array2=np.array([[4,2,8],[7,3,2]])
print(f'2D array is:', numpy_array2)
col_prod=np.prod(numpy_array2,axis=0)
print(f'col_product of 2D array is:', col_prod)

row_prod=np.prod(numpy_array2,axis=1)
print(f'row_product of 2D array is:', row_prod)


