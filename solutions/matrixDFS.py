grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]


def DFS(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])

    if (min(r,c) < 0 or r == ROWS or c == COLS or 
        (r,c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r,c))
    
    count = 0
    count += DFS(grid, r+1, c, visit) #move up
    count += DFS(grid, r-1, c, visit) #move down
    count += DFS(grid, r, c+1, visit) #move right
    count += DFS(grid, r, c-1, visit) #move left

    visit.remove((r,c)) # once the whoe path is visited we remove so that we can visit the same in another path

    return count
