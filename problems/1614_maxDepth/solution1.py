class Solution:
    def maxDepth(self, s: str) -> int:
        res, cur = 0, 0
        for t in s:
            if t == "(":
                cur += 1
                res = max(res, cur)
            elif t == ")":
                cur -= 1
        return res
