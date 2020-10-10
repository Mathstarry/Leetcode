class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        a = 0
        for i in range(1, n):
            a = (a + m) % (i+1)
        return a
