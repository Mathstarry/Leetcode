class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return
        n = len(nums)
        res = [[]]
        for i in range(n):
            l = len(res)
            for t in range(l):
                tmp = res[t].copy()
                tmp.append(nums[i])
                res.append(tmp)
        return res
