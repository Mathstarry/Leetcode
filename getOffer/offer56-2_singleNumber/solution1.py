class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit = [0] * 32
        for t in nums:
            k = 0
            while 1 << k <= t:
                if t & 1 << k != 0:
                    bit[k] += 1
                k += 1
        res = 0
        for i in range(32):
            if bit[i] % 3 == 1:
                res += 1 << i
        return res
