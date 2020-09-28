class Solution:
    def firstUniqChar(self, s: str) -> str:
        p, dct = 0, {}
        for c in s:
            dct[c] = not c in dct
        for c in s:
            if dct[c]: return c
        return " "
