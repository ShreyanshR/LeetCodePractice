from importlib.machinery import SourceFileLoader


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        prevRow = [0] * cols

        for r in range(rows - 1, -1, -1):
            curRow = [0] * cols #current rows are all 0
            curRow[cols - 1] = 1

            for c in range(cols - 2, -1, -1):
                print(f'row, col: {r, c}')
                
                curRow[c] = curRow[c+1] + prevRow[c]
                print(f'row-val, col-val: {curRow[c+1], prevRow[c]}')
            
            prevRow = curRow

        return prevRow[0]


if __name__ == "__main__":
    m,n = 3,7

    S = Solution()

    print(S.uniquePaths(m,n))
