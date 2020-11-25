class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dct = collections.defaultdict(list)
        for k in arr:
            cnt, num = 0, k
            while num > 0:
                if num & 1 == 1:
                    cnt += 1
                num >>= 1
            dct[cnt].append(k)
        res = []
        for k in sorted(dct.keys()):
            res.extend(sorted(dct[k]))
        return res
