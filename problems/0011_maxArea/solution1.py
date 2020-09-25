class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, i, j = 0, 0, len(height) - 1
        while i < j:
            a, b = height[i], height[j]
            res = max(res, min(a, b) * (j-i))
            if a < b:
                i += 1
            elif a > b:
                j -= 1
            else:
                i, j = i + 1, j - 1
        return res
