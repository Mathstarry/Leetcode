class UnionFind:
    def __init__(self, grid):
        # 二维情形的处理
        m, n = len(grid), len(grid[0])
        # 用以记录图中联通分量数
        self.cnt = 0
        self.root = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.root[i * n + j] = i * n + j
                    self.cnt += 1

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            # 路径压缩部分
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.root[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.cnt -= 1

    def getCount(self):
        return self.cnt
