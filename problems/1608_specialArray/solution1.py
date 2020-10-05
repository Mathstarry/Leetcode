class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] >= n: return n
        for x in range(1,n):
            if nums[n-x] >= x > nums[n-x-1]:
                return x
        return -1
