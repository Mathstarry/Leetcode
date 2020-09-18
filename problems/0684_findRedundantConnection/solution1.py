class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 并查集
        n = len(edges)
        # 用字典记录root可以规避索引与值不符的问题
        root = {i:i for i in range(1, n+1)}
        rank = {i:1 for i in range(1, n+1)}
        def find(p, root):
            if p != root[p]:
                root[p] = find(root[p], root)
            return root[p]

        def union(x, y, root):
            rootx, rooty = find(x, root), find(y, root)
            if rootx != rooty:
                if rank[rootx] < rank[rooty]:
                    rootx, rooty = rooty, rootx
                root[rooty] = rootx
                if rank[rootx] == rank[rooty]:
                    rank[rootx] += 1

        def isConnected(p, q, root):
            return find(p, root) == find(q, root)

        for u, v in edges:
            if isConnected(u, v, root):
                return [u, v]
            else:
                union(u, v, root)
