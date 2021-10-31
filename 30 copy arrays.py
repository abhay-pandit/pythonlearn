from numpy import *
'''
arr= array([1,2,3,4,5])

arr= arr+5

print(arr)

arr1= array([1,2,3,4,5])
arr2= array([6,1,9,3,2])

arr3= arr1+arr2

print(arr3)

arr1= array([1,2,3,4,5])
arr2= arr1

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
# same array, not copy in this case.
'''
arr1= array([1,2,3,4,5])
arr2= arr1.copy()

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
