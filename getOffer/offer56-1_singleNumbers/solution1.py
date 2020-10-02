class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        a, n = 0, len(nums)
        for i in range(n):
            a ^= nums[i]
        t = 1
        # 找出 a 最低位的 1
        while a & t == 0: t <<= 1
        # 把数组按照 第 k 位是否为 1 分为两类
        a, b = 0, 0
        for i in range(n):
            if nums[i] & t == 0:
                b ^= nums[i]
            else:
                a ^= nums[i]
        return [a, b]
