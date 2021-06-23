from matrix import *

m1 = Matrix(2, 3)
m2 = Matrix(3, 2)
m1.matrix = [[6, 7, 0], [7, 2, 6]]
m2.matrix = [[5, 3], [1, 1], [5, 1]]
m3 = m1.multiply(m2)
print(m1)
print(m2)
print(m3)
print(m3 == [[37, 25], [67, 29]])
