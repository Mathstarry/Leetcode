class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        b, i = [], 0
        while i < len(A) and A[i] < 0:
            b.append(-A[i])
            i += 1
        a = A[i:]
        b.reverse()
        res, i, j = [], 0, 0
        while i < len(a) or j < len(b):
            numa = a[i] if i < len(a) else float("inf")
            numb = b[j] if j < len(b) else float("inf")
            if numa < numb:
                res.append(numa**2)
                i += 1
            else:
                res.append(numb**2)
                j += 1
        return res
