class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [[0] * (6 * n) for _ in range(n)]
        for j in range(6):
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(i, 6 * (i + 1)):
                for k in range(max(0, j - 6), j):
                    dp[i][j] += dp[i - 1][k]

        total, res = 6 ** n, []
        for j in range(n-1, 6*n):
            res.append(dp[n-1][j] / total)
        return res
