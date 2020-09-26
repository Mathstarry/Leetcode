class Solution:
    def findNthDigit(self, n: int) -> int:
        k, l, cnt = 1, 1, 9
        while n > cnt:
            n -= cnt
            k *= 10
            l += 1
            cnt = 9*k*l
        n -= 1
        q, r = n // l, n % l
        k += q
        return int(str(k)[r])
