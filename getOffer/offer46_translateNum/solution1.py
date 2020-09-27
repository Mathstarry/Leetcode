class Solution:
    def translateNum(self, num: int) -> int:
        # dp[i+1]表示前 i (从0开始)个数有几种翻译方法
        num = str(num)
        dp = [1] * (len(num) + 1)
        for i in range(1, len(num)):
            dp[i+1] = dp[i]
            if '10' <= num[i-1:i+1] <= '25':
                dp[i+1] += dp[i-1]
        return dp[-1]
