class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[] for _ in range(n)]
        res[0] = [[nums[0]]]
        for i in range(1, n):
            for t in res[i-1]:
                for j in range(i+1):
                    tmp = t[:j] + [nums[i]] + t[j:]
                    res[i].append(tmp)
        return res[-1]
