# Ex 4 
# Write a recursive function that determines whether there is a path from the top-left corner (0, 0) to the bottom-right corner (n-1, n-1) in a maze represented by a 2D grid. 
# Maze Rules: 
# •	The maze is a 2D list of booleans (True means you can walk there, False means wall). 
# •	You can move up, down, left, or right — no diagonal moves. 
# •	You may not revisit the same cell twice. 
# •	The start point is always (0, 0). 
# •	The end point is always (n-1, n-1). 

def maze_has_path(maze):
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    rows = len(maze)
    cols = len(maze[0])
    def has_path(i,j):
        if i<0 or i>=rows or j<0 or j>=cols  or maze[i][j]==False or visited[i][j]: 
            return False 
        if i==rows-1 and j==cols -1: 
            return True 
        visited[i][j] = True 
        if has_path(i+1,j) or has_path(i,j+1) or has_path(i-1,j) or has_path(i,j-1): 
            return True 
        return False
    return has_path(0,0)

maze1 = [
    [True,  True,  False],
    [False, True,  False],
    [False, True,  True]
]

print(maze_has_path(maze1))

maze2 = [
    [True,  False, True],
    [False, False, True],
    [True,  True,  True]
]

print(maze_has_path(maze2))

maze3 = [
    [False, True],
    [True,  True]
]

print(maze_has_path(maze3))