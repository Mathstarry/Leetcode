class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        res, l, r = 1, 0, 0
        for i, j in clips:
            if i <= l and j > r:
                r = j
            elif i > l:
                if i > r: break
                l = r
                r = j
                res += 1
            if r >= T:
                break
        return res if r >= T else -1
