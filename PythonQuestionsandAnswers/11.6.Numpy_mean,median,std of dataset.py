#11.3.write a python program that uses numpy to find the mean,median,standard deviation of a dataset.
import numpy as np
import json
with open('C:\\Users\\Lenovo\\Desktop\\sales_dataset.json','r') as file1:
   data=json.load(file1)
   #print(data)

col_data=[dict['unit_price'] for dict in data]
print(col_data)
mean=np.mean(col_data)
print('mean is:', mean)
median=np.median(col_data)
print('median is:', median)
std_dev=np.std(col_data)
print('standard_deviation is:',round(std_dev,4))


