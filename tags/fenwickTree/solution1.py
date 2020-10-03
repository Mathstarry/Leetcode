class FenwickTree:
    # 树状数组
    def __init__(self, n):
        self.size = n
        self.tree = {i: 0 for i in range(1, n+1)}

    def lowbit(self, x):
        return x & (-x)

    def update(self, x, v):
        while x <= self.size:
            self.tree[x] += v
            x += self.lowbit(x)

    def query(self, x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x -= self.lowbit(x)
        return res

