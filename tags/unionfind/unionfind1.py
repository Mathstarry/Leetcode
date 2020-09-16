class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]


    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]


    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.root[rooty] = rootx


    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
