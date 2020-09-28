class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nums = [-1] + heights + [-1]
        stack, res = [], 0
        for i, v in enumerate(nums):
            if not stack or v >= stack[-1][0]:
                stack.append([v, i])
            else:
                while stack[-1][0] > v:
                    cube = stack.pop()
                    res = max(res, cube[0] * (i-stack[-1][1]-1))
                stack.append([v, i])
        return res
