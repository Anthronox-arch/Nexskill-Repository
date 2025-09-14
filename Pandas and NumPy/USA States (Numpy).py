import numpy as np

broker_id, price, bath, street = np.genfromtxt('Work/RealEstate-USA.csv', delimiter = ',', usecols = (0, 2, 4, 6), unpack = True, dtype = None, skip_header = 1, invalid_raise = False)

print(broker_id)
print(price)
print(bath)
print(street)

print()

print("Form 2 Dimensional Array: ")
two_dimensional_array = np.array([price, bath])

print("Two Dimensional Array: ", two_dimensional_array)
print("Dimension of array: ", two_dimensional_array.ndim)
print("Size of array: ", two_dimensional_array.size)
print("Tuple giving size of array: ", two_dimensional_array.shape)
print("Data Types: ", two_dimensional_array.dtype)

print()

two_dimensional_slice = two_dimensional_array [:3, :6]
print(":3, :6 : ", two_dimensional_slice)

two_dimensional_slice_2 = two_dimensional_array[3:10:4]
print(two_dimensional_slice_2)