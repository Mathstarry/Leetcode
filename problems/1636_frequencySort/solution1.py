class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for t in nums:
            freq[t] = freq.get(t, 0) + 1
        dct = {}
        for k, v in freq.items():
            dct[v] = dct.get(v, []) + [k]
        res = []
        for k in sorted(list(dct.keys())):
            for t in sorted(dct[k], reverse=True):
                res += [t] * k
        return res
