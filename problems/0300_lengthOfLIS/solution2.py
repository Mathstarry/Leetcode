class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        res = [nums[0]]
        for i in range(1, n):
            if nums[i] > res[-1]:
                res.append(nums[i])
                continue
            l, r = 0, len(res) - 1
            while l < r:
                m = (l + r) >> 1
                if res[m] < nums[i]:
                    l = m + 1
                else:
                    r = m
            res[l] = nums[i]

        return len(res)
