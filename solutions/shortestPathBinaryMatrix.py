from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    print(length)
                    return length

                directions = [[-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1], [-1,1], [1,-1]]

                for dr, dc in directions:
                    
                    print(f'{r,c}: r & c')
                    print(f'{dr,dc}: dr & dc')
                    #r, c = r + dr, c + dc

                    #print(f'{r,c}: r & c updated'
                    if(min(r + dr, c + dc) < 0 or 
                        r + dr == rows or c + dc == cols or
                        (r + dr, c + dc) in visit or
                        grid[r + dr][c + dc] == 1
                    ):
                        print(f'{r + dr, c + dc}: not traversed')
                        continue
                    
                    print(f'{r + dr, c + dc}: traversed')
                    queue.append((r + dr,c + dc))
                    visit.add((r + dr, c + dc))
                
            length += 1

        return -1

if __name__ == "__main__":
    grid = [[0,1],[1,0]]
    grid = [[0,0,0],[1,1,0],[1,1,0]]

    sol = Solution()
    sol.shortestPathBinaryMatrix(grid)