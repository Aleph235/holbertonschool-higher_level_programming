#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    new_matrix = []
    for inner_list in matrix:
        for element in inner_list:
                squared_matrix.append([element**2 for element in inner_list])
    for element in squared_matrix:
        if element not in new_matrix:
            new_matrix.append(element)
    return new_matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
