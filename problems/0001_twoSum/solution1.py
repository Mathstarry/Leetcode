class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, v in enumerate(nums):
            dct[v] = dct.get(v, []) + [i]
        for k, v in dct.items():
            if target - k in dct:
                if k != target - k:
                    return v + dct[target-k]
                elif len(v) > 1:
                    return v
