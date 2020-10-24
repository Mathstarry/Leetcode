class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        V, n = sum(nums), len(nums)
        if V % 2 == 1 or max(nums) > V // 2: return False
        V //= 2
        dp = [0] * (V+1)
        for i in range(n):
            k = nums[i]
            for j in range(V, k - 1, -1):
                dp[j] = max(dp[j], dp[j-k] + k)
        return True if dp[V] == V else False
