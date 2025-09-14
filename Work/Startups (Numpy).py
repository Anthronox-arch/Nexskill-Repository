import numpy as np

import numpy as np

company, value, country, city = np.genfromtxt('Work/Startups in 2021 end.csv', delimiter = ',', usecols = (1, 2, 4, 5), unpack = True, dtype = None, skip_header = 1, invalid_raise = False)

print(company)
print(value)
print(country)
print(city)

print()

print("Form 2 Dimensional Array")
two_dimension_arrray = np.array([country, city])

print()

print("2 Dimensional Array: ", two_dimension_arrray)
print("Dimension of array 1: ", two_dimension_arrray.ndim)
print("Elements in array 1: ", two_dimension_arrray.size)
print("Tuple giving size of array: ", two_dimension_arrray.shape)
print("Data Type: ", two_dimension_arrray.dtype)

print()

slice_two_dimension = two_dimension_arrray[:1, :4]
print(":1, :4 :", slice_two_dimension)
slice_two_dimension2 = two_dimension_arrray[4:15:4]
print("4:15:4 : ", slice_two_dimension2)