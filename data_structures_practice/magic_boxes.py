# Counting Magic Boxes in a Matrix
# Problem:  
# You are given an n×n matrix of integers. A "magic box" is a 3x3 submatrix within this larger matrix where all the elements are distinct. 
# Your task is to write a function that identifies how many such 3x3 magic boxes exist in the matrix. 


def count_magic_boxes(matrix):
    def is_magic(i,j):
        seen = set()
        for r in range(i,i+3):
            for c in range(j,j+3):
                val = matrix[r][c]
                if val in seen:
                    return False
                else:
                    seen.add(val)
        return True
    rows = len(matrix)
    cols = len(matrix[0])
    magic_conter = 0
    for i in range(rows-2):
        for j in range(cols-2):
            if is_magic(i,j):
                magic_conter += 1
    return magic_conter
            
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7]
]  
print(count_magic_boxes(matrix))

matrix = [
    [1, 2, 3, 9],
    [4, 5, 6, 8],
    [7, 8, 9, 7],
    [1, 2, 3, 4]
]

print(count_magic_boxes(matrix))

