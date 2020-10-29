class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p, q = 0, 0
        while p < len(name) and q < len(typed):
            if name[p] == typed[q]:
                p += 1
                q += 1
            elif p > 0 and typed[q] == name[p-1]:
                q += 1
            else:
                return False
        while q < len(typed):
            if typed[q] == name[p-1]:
                q += 1
            else:
                return False
        return True if p == len(name) and q == len(typed) else False
