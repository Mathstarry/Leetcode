class Solution:
    def minDeletions(self, s: str) -> int:
        freq = collections.defaultdict(int)
        for i in range(len(s)):
            freq[s[i]] += 1
        dct = collections.defaultdict(int)
        for t in freq.values():
            dct[t] += 1
        res = 0
        for t in range(max(dct.keys()), 0, -1):
            if dct[t] > 1:
                tmp = dct[t] - 1
                dct[t] = 1
                dct[t-1] += tmp
                res += tmp
        return res
