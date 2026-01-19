import numpy as np

# the array method can take lists, as well as data type, as arguments
# if not specificied, the data type is float64
a = np.array([1,2,3])
b = np.array([[1,2], [3,4]],dtype = np.float32)

# to initialize arrays with unknown elements:
c = np.zeros((3,4), dtype = np.int32)
d = np.ones((2,2,2), dtype = np.float16)
f = np.empty((2,2), dtype = np.int8)

# arange and linspace generate arrays containing a range of numbers
g = np.arange(0, 10, 2) # array containing numbers between 0 and 10 with 2 increment
h = np.linspace(0,1,10) # array containing 10 numbers between 0 and 1

# for the 3d array 'd'
dim = d.ndim
shape = d.shape
size = d.size
data = d.dtype
print('Array d:')
print(d)
print(f"Dimensions: {dim}\nShape: {shape}\nSize: {size}\nDatatype: {data}")
# notice that dim = len(shape) and size = shape[0]*shape[1]*shape[2]
print('Array f:')
print(f)
print('Array d+f')
print(d+f) # numpy broadcasts a lower dimensional array up to match the higher dimensional array

x = np.arange(0,8,1).reshape(2,2,2)
print('Array x:')
print(x)
print()
print(x.sum(axis=0))    # collapses i dimension
print()
print(x.sum(axis=1))    # collapses j dimension
print()
print(x.sum(axis=2))    # collapses k dimension

# arrays are indexed as x[i,j,k] 
# the i refers to the outermost dimension, j refers to the middle, and k refers to the lowest dimension
# x[i] returns a 2d matrix, x[i,j] returns a 1d matrix, and x[i,j,k] returns a scalar
print(x[1,1,0])

# reshape() returns a changed array, while resize() changes the array itself