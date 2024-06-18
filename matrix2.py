import numpy as np

# Define a sample array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the sum of each row
row_sums = np.sum(array, axis=1)

# Calculate the sum of each column
col_sums = np.sum(array, axis=0)

print("Original array:\n", array)  # Improved formatting for clarity
print("Sum of rows:", row_sums)
print("Sum of columns:", col_sums)