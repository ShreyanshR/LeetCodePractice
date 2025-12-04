from typing import List

class Solution:
    def uniquePath2(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        #print(M,N)

        if grid[M-1][N-1] == 1 or grid[0][0] == 1:
            return 0
        if M == 1 and N == 1 and grid[M-1][N-1] == 0:
            print(M,N)
            print(grid[0][0])
            return 1


        grid[M-1][N-1] = 1

        for r in range(M-1, -1, -1):
            for c in range(N-1, -1, -1):
                if r == M-1 and c == N-1:
                    continue

                if grid[r][c] == 1: #we have reached an obstacle
                    grid[r][c] = 0
                else:
                    down = grid[r+1][c] if r+1 < M else 0 #move down if the row is not out of bounds same of the columns to move right
                    right = grid[r][c+1] if c+1 < N else 0
                    grid[r][c] = right + down
        
        return grid[0][0]


if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,0,0],[0,1,0]]
    grid = [[0,0]]

    S = Solution()
    print(S.uniquePath2(grid))

        