class Solution:
    def totalNQueens(self, n: int) -> int:
        def trackback(row, vst):
            if row == n:
                if self.sign: self.res += 2
                else: self.res += 1
            for j in range(len(col)):
                if col[j] == 1 and all([row+j != x+y and j-row != y-x for x, y in vst]):
                    col[j] = 0
                    vst.add((row, j))
                    trackback(row+1, vst)
                    col[j] = 1
                    vst.remove((row, j))

        self.res, self.sign = 0, True
        col = [1] * n
        for k in range((n+1)//2):
            col[k] = 0
            if n % 2 == 1 and k == n // 2: self.sign = False
            trackback(1, {(0, k)})
            col[k] = 1
        return self.res
