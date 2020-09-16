class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dct = collections.defaultdict(int)
        for i, t in enumerate(answers):
            if t != 0:
                dct[t] += 1
        res = 0
        for k, v in dct.items():
            r = v % (k+1)
            if r > 0:
                res += k + 1 - r
        return res + len(answers)
