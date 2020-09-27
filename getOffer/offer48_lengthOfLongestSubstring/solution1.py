class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vst, res, i, j, tmp = set(), 0, 0, 0, 0
        while j < len(s):
            if s[j] in vst:
                while s[j] in vst:
                    vst.remove(s[i])
                    i += 1
            vst.add(s[j])
            res = max(res, j - i + 1)
            j += 1
        return res
