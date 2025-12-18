# Ex 4 
# Write a recursive function that determines whether there is a path from the top-left corner (0, 0) to the bottom-right corner (n-1, n-1) in a maze represented by a 2D grid. 
# Maze Rules: 
# •	The maze is a 2D list of booleans (True means you can walk there, False means wall). 
# •	You can move up, down, left, or right — no diagonal moves. 
# •	You may not revisit the same cell twice. 
# •	The start point is always (0, 0). 
# •	The end point is always (n-1, n-1). 

def has_path(maze,i,j):
    if i<0 or i>=len(maze) or j<0 or j>=len(maze[0]) or maze[i][j]==False:
        return False
    if i==len(maze)-1 and j==len(maze[0])-1:
        return True
    
    original = maze[i][j] 
    maze[i][j] = False
    if has_path(maze,i+1,j) or has_path(maze,i,j+1) or has_path(maze,i-1,j) or has_path(maze,i,j-1):
        return True
    maze[i][j] = original
    return False
    
maze1 = [
    [True,  True,  False],
    [False, True,  False],
    [False, True,  True]
]

print(has_path(maze1, 0, 0))

maze2 = [
    [True,  False, True],
    [False, False, True],
    [True,  True,  True]
]

print(has_path(maze2, 0, 0))

maze3 = [
    [False, True],
    [True,  True]
]

print(has_path(maze3, 0, 0))

    
    

