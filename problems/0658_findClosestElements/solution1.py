class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            m = math.ceil((l + r) / 2)
            if arr[m] <= x:
                l = m
            else:
                r = m - 1

        t, r = k + 1, l
        while t > 0:
            if l <= 0: return arr[:k]
            if r >= len(arr): return arr[-k:]
            a, b = x - arr[l], arr[r] - x
            if a <= b:
                l -= 1
            else:
                r += 1
            t -= 1
        return arr[l+1: r]
