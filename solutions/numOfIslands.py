import collections
from re import X
from typing import List

class Solution:
    def numOfIslands(self, grid: List[List[str]])-> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        isIslands = 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def BFS(r,c):
            q = collections.deque()
            visit.add(r,c)
            q.append((r,c))

            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r, c = r + dr, c + dc

                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.append((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    BFS(r,c)
                    isIslands += 1       

        