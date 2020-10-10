class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, minV = 0, float("inf")
        for i in range(len(prices)):
            minV = min(minV, prices[i])
            res = max(res, prices[i] - minV)
        return res
