#Given a list of lists create a 2D NumPy array and find the sum of elements in each row and column.
import numpy as np
lists=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
Two_D_array=np.array(lists)
print('2D array is:', Two_D_array)

rows_sum=np.sum(Two_D_array, axis=0)
print('sum of rows:', rows_sum)
col_sum=np.sum(Two_D_array, axis=1)
print('sum of columns:', col_sum)