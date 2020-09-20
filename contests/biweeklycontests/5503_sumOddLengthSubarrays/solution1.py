class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for l in range(1, n+1, 2):
            i, j = 0, l-1
            tmp = sum(arr[i:j+1])
            res += tmp
            while j < n - 1:
                j += 1
                tmp += arr[j] - arr[i]
                res += tmp
                i += 1
        return res
