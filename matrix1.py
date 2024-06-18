import numpy as np

def transpose_matrix(matrix):
    return np.transpose(matrix)

input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

output_matrix = transpose_matrix(input_matrix)

print('input')
print(input_matrix)
print('output')
print(output_matrix)