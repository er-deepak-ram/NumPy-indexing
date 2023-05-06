import numpy as np

one_d_arr = np.array([1, 2, 3, 4, 5])
print(one_d_arr[0])

two_d_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element in 1st row: ",two_d_arr[0][1])
print("5th element in 2nd row: ", two_d_arr[1][4])

three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(three_d_arr[0][1][2])
