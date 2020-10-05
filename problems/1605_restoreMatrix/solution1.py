class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        grid = [[0] * m for _ in range(n)]
        for i in range(n):
            if rowSum[i] == 0: continue
            for j in range(m):
                grid[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= grid[i][j]
                colSum[j] -= grid[i][j]
        return grid
