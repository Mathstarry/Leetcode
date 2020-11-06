class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        # dp[i][j] 表示列表中取前i个，目标中取前j个，有几种取法
        n, m, s = len(words), len(words[0]), len(target)
        dct = [collections.defaultdict(int) for _ in range(m)]
        for i in range(m):
            for word in words:
                t = word[i]
                dct[i][t] += 1

        dp = [[0] * (s + 1) for _ in range(m + 1)]
        for i in range(m+1):
            dp[i][0] = 1
        for j in range(1, s + 1):
            k = target[j - 1]
            for i in range(1, m + 1):
                dp[i][j] = dp[i - 1][j - 1] * dct[i-1][k] + dp[i - 1][j]
                dp[i][j] %= MOD
        return dp[-1][-1]
