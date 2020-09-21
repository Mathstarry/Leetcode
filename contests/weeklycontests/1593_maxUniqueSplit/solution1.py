class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def recur(a, idx):
            if idx == n:
                self.res = max(self.res, len(a))
                return

            for l in range(1, n - idx + 1):
                if len(a) + 1 + n - (idx + l) <= self.res:
                    break
                if s[idx: idx + l] not in a:
                    recur(a + [s[idx: idx + l]], idx + l)

        self.res, n = 1, len(s)
        recur([], 0)
        return self.res
        
