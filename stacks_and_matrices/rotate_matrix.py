# You are given an n×n matrix. Write a function to rotate the matrix by 90 degrees clockwise
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# =>
# rotated = [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]


def rotate_matrix(matrix):
    rotated = []
    for _ in range(len(matrix)):
        rotated.append([])
    for row in range(len(matrix)-1,-1,-1):
        for index,num in enumerate(matrix[row]):
            rotated[index].append(num)
    return rotated

# 90° clockwise rotation = transpose + reverse each row

def rotate_matrix_inplace(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            temp = matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp
    for row in matrix:
        row.reverse()
    return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(matrix))
print(rotate_matrix_inplace(matrix))


