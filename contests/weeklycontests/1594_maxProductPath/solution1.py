class Solution:
    def maxProductPath(self, grid) -> int:
        mod = 10 ** 9 + 7
        n, m = len(grid), len(grid[0])
        # 维护目前的最大值与最小值
        dp = [[[-1, 1] for j in range(m)] for i in range(n)]
        dp[0][0] = [grid[0][0], grid[0][0]]
        hasZero = False if grid[0][0] else True
        for i in range(1, n):
            dp[i][0][1] = dp[i][0][0] = dp[i-1][0][0] * grid[i][0]
        if dp[-1][0][0] == 0: hasZero = True
        for j in range(1, m):
            dp[0][j][1] = dp[0][j][0] = dp[0][j-1][0] * grid[0][j]
        if dp[0][-1][0] == 0: hasZero = True
        for i in range(1, n):
            for j in range(1, m):
                arr = [dp[i-1][j][1], dp[i][j-1][1], dp[i-1][j][0], dp[i][j-1][0]]
                for k in range(4):
                    arr[k] *= grid[i][j]
                pos, neg = max(arr), min(arr)
                dp[i][j] = [pos, neg]

        res = 0 if hasZero else -1
        return dp[n - 1][m - 1][0] % mod if dp[n - 1][m - 1][0] >= 0 else res
