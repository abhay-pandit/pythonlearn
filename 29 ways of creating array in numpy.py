'''
array()
linespace()
logspace()
arange()
zeros()
ones()
'''

from numpy import *

arr= array([1,2,3,4,5])

print(arr.dtype)

arr= linspace(0,15,16)

print(arr)

arr= linspace(0,15,20)

print(arr)
arr= linspace(0,15)

print(arr)


arr= logspace(1,40,5)

print(arr)


arr= zeros(3)

print(arr)

arr= ones(3)

print(arr)