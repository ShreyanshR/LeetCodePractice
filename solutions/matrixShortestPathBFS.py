from collections import deque
from typing import List
from winreg import ConnectRegistry

grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))
        len = 0

        while queue:
            r, c = queue.popleft()

            #check if we have reached the last row & column
            if r == rows - 1 and c == cols - 1:
                return len
            
            neighbors = [[1,0], [-1,0], [0,1], [0,-1]]
            
            for dr, dc in neighbors:
                r, c = r + dr, c + dc

                if (min(r,c) < 0 or r == rows or c == cols or
                    (r,c) in visit or grid[r][c] == 1
                    ):
                    continue

                queue.append(r,c)
                visit.add(r,c)
            len += 1

            return len
