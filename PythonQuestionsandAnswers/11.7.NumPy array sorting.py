#11.7. Create a function that takes a list of numbers and returns the numpy array sorted in ascending
#return order.

import numpy as np

def array_sorting(list1):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                list1[i],list1[j]=list1[j],list1[i]
    return (np.array(list1))


list1=[9,6,3,8,1,2]
result=array_sorting(list1)
print(result)
