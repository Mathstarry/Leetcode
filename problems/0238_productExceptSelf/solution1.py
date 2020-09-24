class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre 和 suf 分别表示第 i 个数字的前缀积与后缀积（不包括数字nums[i]）
        n = len(nums)
        pre, suf, res = 1, 1, [1] * n
        for i in range(1, n):
            pre *= nums[i-1]
            res[i] *= pre
        for j in range(n-2, -1, -1):
            suf *= nums[j+1]
            res[j] *= suf
        return res
