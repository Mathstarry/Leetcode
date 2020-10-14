class Solution:
    def sumNums(self, n: int) -> int:
        self.res = 0
        def recur(n):
            self.res += n
            return not n or recur(n-1)
        recur(n)
        return self.res
