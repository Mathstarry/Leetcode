class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        # 去重
        dct = {v: i for i, v in enumerate(nums)}
        s = sorted(dct.keys())
        # 离散化数组，将其转化为 1~n
        idx = {v: i+1 for i, v in enumerate(s)}
        for i in range(n):
            nums[i] = idx[nums[i]]
        
        fwt = FenwickTree(n)
        for t in nums[::-1]:
            # 更新节点
            fwt.update(t, 1)
            # 计算前缀和
            res += fwt.query(t-1)
        return res

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
