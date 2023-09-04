#11.12. Given a numpy array, calculate the dot product of the array with itself.

import numpy as np
arr=np.random.randint(5,15,(3,3))
print('NumPy array is:\n', arr,'\n')

dot_product=np.dot(arr,arr)
print('dot_product of array with itself is:')
for row in dot_product:
    print(row)

# def matrix_mult(A,B):
#     if len(A[0])!=len(B):
#         raise ValueError('Number of columns in matrix A must be equal to number of rows in matrix B')
#
#     result=[[0 for _ in range(len(B[0]))] for _ in range(len(A))]
#     #print(result)
#
#     for i in range(len(A)):
#         for j in range(len(B[0])):
#             for k in range(len(B)):
#                 result[i][j]+=A[i][k]*B[k][j]
#     return result
#
# A=[[1,2,3],[4,5,6]]
# B=[[1,2,3],[4,5,6],[7,8,9]]
#
# result=matrix_mult(A,B)
# print('Matrices A and B multiplication is', result)
# for row in result:
#     print(row)
#







