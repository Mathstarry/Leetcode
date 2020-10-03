class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        if nums[0] > 0:
            if all([nums[i] == nums[i-1]+1 for i in range(1,5)]):
                return True
            return False
        else:
            l = 0
            while nums[l] == 0: l += 1
            if l >= 4: return True
            if all([nums[i] != nums[i+1] for i in range(l, 4)]) and nums[4] - nums[l] <= 4:
                return True
            return False
