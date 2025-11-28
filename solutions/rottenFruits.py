from typing import FrozenSet, List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        mins = 0

        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0: 
            for i in range(len(q)):
                r, c = q.popleft()
                print(r,c)
                
                dirs = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    #print(f'{nr, nc},{grid[nr][nc]}: position, value')

                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1
                        ):
                        print("rotten fruit")
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

                        print(f'{nr, nc}: rotten fruit position')
                        print(f'{grid[nr][nc]}: rotten fruit')

            mins += 1

        return mins if fresh == 0 else -1

if __name__ == "__main__":
    grid = [[1,1,0],[0,1,1],[0,1,2]]

    S = Solution()
    S.orangesRotting(grid)