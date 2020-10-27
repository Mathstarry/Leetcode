class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        i, j, res = 0, 1, 0
        while j < len(A):
            res = max(res, A[j] + A[i] + i - j)
            if A[i] - A[j] <= j - i:
                i = j
            j += 1
        return res
