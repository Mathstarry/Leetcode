class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k == 0: return 1
        if 0 < k < n: return 0
        if k == n**2: return 1
        # 因为 n <= 6，所以这里直接用字典记录了n!的值，也可以写一个迭代函数去计算
        fact = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720}
        
        def choose(n, k):
            return fact[n] // (fact[k] * fact[n-k])
        
        res = 0
        for r in range(n+1):
            for c in range(n+1):
                t = r * n + c * n - c * r
                if t == k:
                    res += choose(n, c) * choose(n, r)
        return res
