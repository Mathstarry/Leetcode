class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def divid(l, r, k):
            while l <= r:
                m = (l + r) >> 1
                if nums[m] <= k:
                    l = m + 1
                else:
                    r = m - 1
            return r
        right = divid(0, len(nums)-1, target)
        if right >= 0 and nums[right] != target: return 0
        left = divid(0, right, target - 1)
        return right - left
