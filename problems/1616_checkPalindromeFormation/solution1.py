class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        def f(x, y):
            l, r = 0, n - 1
            while l <= r and x[l] == y[r]:
                l += 1
                r -= 1
            s, t = l, r
            while l <= r and y[l] == y[r]:
                l += 1
                r -= 1
            while s <= t and x[s] == x[t]:
                s += 1
                t -= 1
            return True if l > r or s > t else False
        
        return f(a, b) or f(b, a) or f(a, a) or f(b, b)
