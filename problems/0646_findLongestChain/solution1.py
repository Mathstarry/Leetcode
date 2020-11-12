class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        prel, prer, res = float("-inf"), float("-inf"), 0
        for l, r in pairs:
            if l > prer:
                res += 1
                prer = r
            elif r < prer:
                prer = r
        return res
