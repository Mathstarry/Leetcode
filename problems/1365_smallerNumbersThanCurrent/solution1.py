class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        dct = collections.defaultdict(list)
        for i, v in enumerate(nums):
            dct[v].append(i)
        nums.sort()
        for i, t in enumerate(nums):
            if i == 0 or nums[i] > nums[i-1]:
                for j in dct[t]:
                    res[j] = i
        return res
