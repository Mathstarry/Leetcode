class Solution:
    def strToInt(self, str: str) -> int:
        s = str.strip() + "?"
        re = "+-0123456789"
        if s[0] not in re: return 0
        i = 1
        while s[i].isdigit(): i += 1
        if i == 1 and not s[0].isdigit(): return 0
        res = int(s[:i])
        if res < -2**31: return -2**31
        elif res >= 2**31: return 2**31 - 1
        return res
