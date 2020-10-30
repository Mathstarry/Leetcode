class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dct = {v: i for i, v in enumerate(S)}
        l, r, res = 0, 0, []
        for i, v in enumerate(S):
            r = max(r, dct[v])
            if i == r:
                res.append(r - l + 1)
                l = r + 1
        return res
