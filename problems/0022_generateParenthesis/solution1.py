class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def recur(s, l, r):
            if r == 0:
                self.res.append(s)
                return
            if l > 0:
                recur(s+"(", l-1, r)
            if l < r:
                recur(s+")", l, r-1)
                
        recur("", n, n)
        return self.res
