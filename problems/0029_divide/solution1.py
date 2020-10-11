class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        n, d = abs(dividend), abs(divisor)
        res, k = 0, 31
        while n >= d:
            while n >> k < d: k -= 1
            n -= d << k
            res += 1 << k
        
        res = res if sign == 1 else -res
        return res if res < (1 << 31) else (1 << 31) - 1
