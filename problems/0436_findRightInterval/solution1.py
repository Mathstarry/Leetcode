class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dct = {v[0]: i for i, v in enumerate(intervals)}
        intervals.sort()
        res = [-1] * len(intervals)
        for i, v in enumerate(intervals):
            l, r = i + 1, len(intervals) - 1
            if intervals[r][0] < v[1]: continue
            k = dct[v[0]]
            while l < r:
                m = (l + r) >> 1
                if intervals[m][0] < v[1]:
                    l = m + 1
                else:
                    r = m
            res[k] = dct[intervals[l][0]]
        return res
