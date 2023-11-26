# Creating a 2D array with 3 rows and 4 columns, initialized with zeros
rows = 3
columns = 3
two_d_array = [[0] * columns for _ in range(rows)]

# Accessing and updating elements in the 2D array
two_d_array[0][1] = 5
two_d_array[2][2] = 10

# Displaying the 2D array
for row in two_d_array:
    print(row)