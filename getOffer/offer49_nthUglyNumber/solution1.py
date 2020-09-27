class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p, q, res = [0] * 3, [2, 3, 5], [1]
        while n - 1 > 0:
            t = min([res[p[k]] * q[k] for k in range(3)])
            res.append(t)
            for i in range(3):
                if res[p[i]] * q[i] == t:
                    p[i] += 1
            n -= 1

        return res[-1]
