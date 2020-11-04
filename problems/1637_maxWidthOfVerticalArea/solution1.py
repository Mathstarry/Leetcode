class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res = 0
        points.sort()
        prev = points[0][0]
        for x, y in points[1:]:
            res = max(res, x - prev)
            prev = x
        return res
