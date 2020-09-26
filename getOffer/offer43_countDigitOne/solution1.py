class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        m = len(s)
        # dp[i] 表示后 [1, 10^(i+1))中 1 出现的次数
        dp = [0] * m
        dp[0] = 1
        for i in range(1, m):
            dp[i] = 10 * dp[i-1] + 10**i
        res = 0
        for i in range(m-1):
            res += dp[m-2-i] * int(s[i])
            if int(s[i]) > 1:
                res += 10**(m-1-i)
            elif int(s[i]) == 1:
                res += int(s[i+1:]) + 1
        if int(s[-1]) != 0:
            res += 1
        return res
