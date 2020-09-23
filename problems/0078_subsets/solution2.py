class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        l = 1 << n
        for i in range(l):
            cur = []
            for j in range(n):
                if (i >> j) & 1 == 1:
                    cur.append(nums[j])
            res.append(cur)
        return res
