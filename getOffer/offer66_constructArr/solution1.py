class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res, l, r = [1] * len(a), 1, 1
        for i in range(1, len(a)):
            l *= a[i-1]
            r *= a[len(a)-i]
            res[i] *= l
            res[len(a)-i-1] *= r
    
        return res
