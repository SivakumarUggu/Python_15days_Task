#Create a numpy array from a python list and perform basic operations like addition, multiplication, etc.
import numpy as np
list1=[2,4,3,1,5]
numpy_array=np.array(list1)
print(numpy_array)

#Addition
print(numpy_array+10)
#Multiplication
print(numpy_array*3)

#Elementwise Addition with another array
addition_of_two_arrays=numpy_array+np.array([8,5,3,2,4])
print(addition_of_two_arrays)
#Elementwise multiplication of two arrays
arrays_mult=numpy_array*np.array([8,5,3,2,4])
print(arrays_mult)

#Sum of array
sum=np.sum(numpy_array)
print(sum)

#Mean of array
mean=np.mean(numpy_array)
print(f'%.2f'%mean)



