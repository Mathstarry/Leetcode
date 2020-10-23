class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dct, res = {}, -1
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = i
            else:
                res = max(res, i - dct[s[i]] - 1)
        return res
