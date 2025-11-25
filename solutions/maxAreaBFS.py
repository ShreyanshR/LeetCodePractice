from typing import List
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        area = 0

        directions = [[1,0], [-1, 0], [0,1], [0, -1]]

        def BFS(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            
            res = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if((nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == 1 and
                        (nr,nc) not in visit
                    )):
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        res += 1

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = max(area, BFS(r,c))

        return area
