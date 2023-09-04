#11.10. Write a function that takes a numpy array and returns new array with all elements squared.

import numpy as np

def elements_squreing(Numpy_array):
    print('Original Numpy arr:', Numpy_array)
    squared_list=[]
    for ele in Numpy_array:
        squared_ele=ele**2
        squared_list.append(squared_ele)
    squared_arr=np.array(squared_list)
    return squared_arr

list1=[1,2,3,4,5]
Numpy_array=np.array(list1)
result=elements_squreing(Numpy_array)
print('squared numpy arr:', result)