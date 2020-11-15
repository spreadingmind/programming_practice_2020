#!/usr/bin/env python
# coding: utf-8

# In[665]:


import numpy as np
import matplotlib.pyplot as plt
from random import randint
from time import time


# In[745]:


# 1 
# create numpy matrix 100*2
np_values = np.random.randint(1000,size=(100, 2))
# create standard matrix 100*2
values_std = [[randint(0, 1000), randint(0, 1000)] for i in range(100)]
np_time = []
std_time = []

def f(x, y):
    return 2*x**2 + 4*y

def numpy_f(arr):
    res = 2*arr.T[0]**2 + 4*arr.T[1]
        
def std_f(arr):
    return [f(x, y) for (x, y) in arr]

# time 100 iterations of numpy and standard func
for i in range(100):
    start = time()
    numpy_f(np_values)
    end = time()
    np_time.append(end - start)
    
for i in range(100):
    start = time()
    numpy_f(np_values)
    end = time()
    std_time.append(end - start)

# build exec time stats plot 
plt.plot(np_time)
plt.plot(std_time)
plt.show()


# In[2]:


# 2

# create array of ints from 2 to 75
arr = np.arange(2, 76, 1)
# get odd numbers
odd = arr[arr % 2 == 1]
print(odd)
# change all odd numbers to -1
arr_subst = np.where(arr % 2 == 0, arr, -1)
print(arr_subst)


# In[797]:


# 3

base_arr = np.array([1, 2, 3, 4, 6, 6, 7, 8])
arr2 = [1, 2, 3, 4]

# delete by value
arr1 = base_arr
arr1 = np.delete(arr1, np.argwhere(arr1 == arr2[0]))
print(arr1)

# delete by values from another array
arr1 = base_arr
for e in arr2:
    arr1 = np.delete(arr1, np.argwhere(arr1 == e))
print(arr1)

# delete by indexes
arr1 = base_arr
arr1 = np.delete(arr1, [0, 1])
print(arr1)


# In[799]:


# 4
# create matrix of random numbers and size from 2 to 10
s = np.random.randint(2, 11) 

# divide each element by max value
matrix_rand_1 = np.random.randint(s, size=(s, s))
max_value = matrix_rand_1.max()
matrix_rand_1[matrix_rand_1] = matrix_rand_1 / max_value

# substract row average value from each row 
matrix_rand_2 = np.random.randint(s, size=(s, s))
mean_row_values = np.mean(matrix_rand_2, axis = 1)

for i in range(s):
    mean = mean_row_values[i]
    matrix_rand_2[i, :] -= int(mean)

# change max value to -1
matrix_rand_3 = np.random.randint(s, size=(s, s))
max_value = matrix_rand_3.max()
matrix_rand_3[matrix_rand_3 == max_value] = -1


# In[805]:


# 5
# create matrix of random float numbers and size from 2 to 10
s = np.random.randint(2, 11) 
m_1 = np.random.uniform(low=1.0, high=101.0, size=(s,s))
mean_value = np.mean(m_1)
print(mean_value)

# fill matrix with nans randomly using mask
nans_number = np.random.randint(1, s*s)
mask = np.zeros(s*s, dtype=bool)
mask[:nans_number] = True
np.random.shuffle(mask)
mask = mask.reshape(s, s)
m_1[mask] = np.nan

if np.isnan(m_1).all():
    # fill nans with zeros if all elemetns are nans
    m_1 = np.nan_to_num(m_1, nan=0)
else:
    # fill nans with matrix mean value
    m_1 = np.nan_to_num(m_1, nan=mean_value)


# In[796]:


# 6
# create random matrix of size from 2 to 6
s = np.random.randint(2, 6)
matrix_rand = np.random.randint(low=-10, high=11, size=(s, s))
# normalize matrix
norm = np.linalg.norm(matrix_rand)
normal_array = matrix_rand/norm
normal_array


# In[431]:


# 7
# load matrix from file
m = np.loadtxt("matrix.txt")

# modify matrix
m = m / 2

# write matrix to file
np.savetxt('martix_out.txt', m, delimiter = ' ')


# In[569]:


# 8
val = 50
s = np.random.randint(10, 101)
matrix_rand = np.random.randint(s, size=(s, s))
# get matrix element closest to val
closest_to_val = matrix_rand.flat[np.abs(matrix_rand - val).argmin()]


# In[809]:


# 9 
m = np.random.randint(1, 20)
n = np.random.randint(1, 20)

# fill matrix with zeros
matrix = np.full((m, n), 0, dtype=int)

# change border values to 1
matrix[:,[0,-1]] = matrix[[0,-1]] = 1


# In[811]:


# 10
s = np.random.randint(2, 11)
matrix_rand = np.random.randint(low=-10, high=11, size=(s, s))
print(matrix_rand)
# get column number from input
col_to_sort = int(input('Column to be sorted by'))
# sort matrix by given column in decreasing order
matrix_rand = matrix_rand[matrix_rand[:,col_to_sort].argsort()[::-1]]
print(matrix_rand)


# In[666]:


# 11
board_size = (8, 8)
# fill board with zeros
matrix = np.zeros(board_size,dtype=int)
# change every second value to 1
matrix[1::2,::2] = 1
matrix[::2,1::2] = 1
