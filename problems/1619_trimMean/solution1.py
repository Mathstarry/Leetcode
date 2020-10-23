class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        k = n // 20
        lst = arr[k:]
        lst = lst[:-k]
        res = sum(lst) / (n - 2*k)
        return res
