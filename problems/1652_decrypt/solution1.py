class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0: return res
        tar = 0
        if k > 0:
            t = 0
            while t < k:
                t = t + 1
                tar += code[t]
            for i in range(n):
                res[i] = tar
                t = (t + 1) % n
                tar = tar - code[(i+1)%n] + code[t]
        elif k < 0:
            t = -1
            while t >= k:
                tar += code[t]
                t -= 1
            for i in range(n):
                res[i] = tar
                t = (t + 1) % n
                tar = tar + code[i] - code[t]
        return res
