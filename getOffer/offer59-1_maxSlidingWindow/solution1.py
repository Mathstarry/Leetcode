class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 维护一个单调递减栈
        stack, res = [], []
        for i in range(len(nums)):
            if stack and stack[0] == i - k:
                stack.pop(0)
            if not stack or nums[stack[-1]] >= nums[i]:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                stack.append(i)
            if i >= k - 1:
                res.append(nums[stack[0]])
        return res
