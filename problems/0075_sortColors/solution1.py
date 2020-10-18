class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, c = 0, len(nums) - 1, 0
        while c <= r:
            if nums[c] == 1 or l > c:
                c += 1
            elif nums[c] == 0:
                nums[c], nums[l] = nums[l], nums[c]
                l += 1
            elif nums[c] == 2:
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1
