class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n, res = len(nums), 0
        tag = [0] * (n+1)
        coef = [0] * n

        # tag用以记录每一个位置上start和end的数量之差
        for s, e in requests:
            tag[s] += 1
            tag[e+1] -= 1
        # coef用以记录前i个位置累积start和end的数量之差
        coef[0] = tag[0]
        for i in range(1, n):
            coef[i] = coef[i-1] + tag[i]

        coef.sort(reverse=True)
        nums.sort(reverse=True)
        # 依次让数组中最大的数字与coef最大的数字相乘
        for i in range(n):
            res += coef[i] * nums[i]
            res %= mod
        return res
        
