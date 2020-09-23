class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[i][j] 标记前 i 个数字以 j+1 结尾的组合数
        dp = [[1] * 6 for _ in range(n+1)]
        for i in range(2, n+1):
            for j in range(6):
                dp[i][j] = sum(dp[i-1])
                if i - rollMax[j] > 1:
                    dp[i][j] = dp[i][j] - sum(dp[i-rollMax[j]-1]) + dp[i-rollMax[j]-1][j]
                elif i - rollMax[j] == 1:
                    dp[i][j] -= 1

        return sum(dp[n]) % (10 ** 9 + 7)
