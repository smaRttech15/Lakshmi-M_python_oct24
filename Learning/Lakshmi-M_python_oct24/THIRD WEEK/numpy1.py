import numpy as np
import scipy

array1 = np.arange(10)
array2 = np.arange(10,20)
array3 = np.arange(10,30,3)

print(type(array1))
print(array2)

arr = np.arange(1,10)
print(arr,'\n')
arr = arr.reshape(3,3)
print(arr,'\n')
arr = arr.reshape(9)
print(arr,'\n')
#arr = arr.reshape(2,4) print(arr,'\n')            (value error)


arr = np.arange(1,10).reshape(3,-1)  #here python decides no of cloumnes
print(arr)
arr = np.arange(2,25,2).reshape(-1,4)   #here python decides no of rows
print (arr)
#(-1,-1) error

arr = np.array([[2,4,6,8],[9,19,4,10]])
array2 = arr+5 #broadcasting
print(arr)
print(array2)