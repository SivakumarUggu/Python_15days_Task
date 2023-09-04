#Generate a numpy array of random numbers and calculate its mean,median, and standard deviation.
import numpy as np
array_of_rand=np.random.rand(100)
print(array_of_rand)
#Mean
array_mean=np.mean(array_of_rand)
array_median=np.median(array_of_rand)
array_std=np.std(array_of_rand)
print(f'array mean is:%.4f'%array_mean)
print('array median is:%.4f'%array_median)
print('array standard deviation is:%.4f'%array_std)