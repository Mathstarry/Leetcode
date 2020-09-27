class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def fast_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while nums[l] + nums[j] <= nums[j] + nums[l] and i < j: j -= 1
                while nums[i] + nums[l] <= nums[l] + nums[i] and i < j: i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            fast_sort(l, i-1)
            fast_sort(i+1, r)

        nums = list(map(str, nums))
        fast_sort(0, len(nums)-1)
        return "".join(nums)
