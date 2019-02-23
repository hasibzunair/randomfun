from numpy import array

# ref: https://machinelearningmastery.com/index-slice-reshape-numpy-arrays-machine-learning-python/


data = [11, 22, 33, 44, 55]
data_2d = [[11, 22], [33, 44], [55, 66]] 

data = array(data)

# first row first elem
#print(data[0][1])

# first row all elems
#print(data[0,])


#print(data[0,1])
#print(data[0][0])

#print(data[-2:])
#print(data[:-2])


data_3d = array([[11, 22, 33],
		[44, 55, 66],
		[77, 88, 99]])
# separate data
X, y = data_3d[:, :-1], data_3d[:, -1]

# all values excepts last column
print(X)
# last column
print(y)
