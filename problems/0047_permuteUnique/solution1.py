class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recur(s, rest, l):
            if l == n:
                res.append(s.copy())
                return
            for i in range(n):
                # 同层之间相同数字只放第一个出现的
                if i > 0 and nums[i] == nums[i-1] and rest[i-1] == 1:
                    continue
                if rest[i] == 1:
                    rest[i] = 0
                    s.append(nums[i])
                    recur(s, rest, l + 1)
                    rest[i] = 1
                    s.pop()

        nums.sort()
        n, res = len(nums), []
        rest = [1] * n
        recur([], rest, 0)
        return res
