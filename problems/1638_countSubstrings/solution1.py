class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def isSame(a, b):
            cnt = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                  cnt += 1
                if cnt > 1: return False
            return True if cnt == 1 else False
        
        res, vst = 0, {}
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] in vst:
                    res += vst[s[i:j]]
                    continue
                l, cnt = j - i, 0
                for k in range(len(t) - l + 1):
                    if isSame(s[i:j], t[k:k+l]):
                        cnt += 1
                res += cnt
                vst[s[i:j]] = cnt
        return res
