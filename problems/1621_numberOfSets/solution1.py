class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][t] 表示区间[0,i]中取j+1段有几种取法, t=0 不取, t=1 取新一段, t=2 和前一段连起来
        dp = [[[0, 0, 0] for t in range(k+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0][0] = 1
        for i in range(1, n):
            for j in range(1, min(i, k)+1):
                dp[i][j][0] = sum(dp[i-1][j])
                dp[i][j][1] = sum(dp[i-1][j-1])
                dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
        return sum(dp[n-1][k]) % MOD
