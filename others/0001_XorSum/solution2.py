class Solution:
    def XorSum(self, nums):
        # 整合版
        def mono(nums, isMin):
            res, stack, i = 0, [-1], 0
            s = 1 if isMin else -1
            lst = nums.copy()
            lst += [-1] if isMin else [float("inf")]
            while i < n or stack[-1] >= 0:
                while stack[-1] >= 0 and lst[stack[-1]]*s > lst[i]*s:
                    p = stack.pop()
                    if ((i - p) * (p - stack[-1])) % 2 == 1:
                        res ^= lst[p]
                if i < n:
                    stack.append(i)
                    i += 1
            return res

        n = len(nums)
        return mono(nums, 1) ^ mono(nums, 0)
