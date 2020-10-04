class Solution:
    def XorSum(self, nums):
        # 基础版
        stackMin, stackMax = [-1], [-1]
        res, n = 0, len(nums)
        for i in range(n):
            while stackMin[-1] >= 0 and nums[stackMin[-1]] > nums[i]:
                p = stackMin.pop()
                if ((i - p) * (p - stackMin[-1])) % 2 == 1:
                    res ^= nums[p]
            stackMin.append(i)
            while stackMax[-1] >= 0 and nums[stackMax[-1]] < nums[i]:
                q = stackMax.pop()
                if ((i - q) * (q - stackMax[-1])) % 2 == 1:
                    res ^= nums[q]
            stackMax.append(i)
        while stackMin[-1] >= 0:
            p = stackMin.pop()
            if ((n - p) * (p - stackMin[-1])) % 2 == 1:
                res ^= nums[p]
        while stackMax[-1] >= 0:
            q = stackMax.pop()
            if ((n - q) * (q - stackMax[-1])) % 2 == 1:
                res ^= nums[q]

        return res
