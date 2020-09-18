class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # 记录入度为2的点和入度为0的点，两者都只有不存在或存在一点两种可能
        indeg2, indeg0, indeg = -1, -1, {}
        for u, v in edges:
            indeg[v] = indeg.get(v, []) + [u]
            if len(indeg[v]) == 2:
                indeg2 = v
        n = len(edges)
        for i in range(1, n+1):
            if i not in indeg:
                indeg0 = i
                break
        # 若存在根节点(入度为0)，则必存在有且只有一个入度为2的点
        if indeg0 != -1:
            a, b = indeg[indeg2]
            # 去掉在环中的那条边即可
            p = a
            while p != indeg0 and p != indeg2:
                p = indeg[p][0]
            pre = a if p == indeg2 else b
            return [pre, indeg2]

        # 若不存在根节点，则不存在入度为2的点，且存在一个loop
        root = {i: i for i in range(1, n+1)}

        def find(p, root):
            if root[p] != p:
                root[p] = find(root[p], root)
            return root[p]

        # x指向y，所以y的父节点必须是x
        def union(x, y, root):
            rootx, rooty = find(x, root), find(y, root)
            if rootx != rooty:
                root[rooty] = rootx
        # 所有点入度为1，如遇到两点的root相同，则是出现了环
        for u, v in edges:
            if find(u, root) != find(v, root):
                union(u, v, root)
            else:
                return [u, v]
