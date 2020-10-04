class Solution:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums

    def getIntval(self, nums):
        res, stack, n = 0, [-1], len(nums)
        for i in range(n):
            while stack[-1] >= 0 and nums[stack[-1]] > nums[i]:
                h = stack.pop()
                res = max(res, (i - stack[-1] - 1) * nums[h])
            stack.append(i)
        while stack[-1] >= 0:
            h = stack.pop()
            res = max(res, (n - stack[-1] - 1) * nums[h])
        return res
