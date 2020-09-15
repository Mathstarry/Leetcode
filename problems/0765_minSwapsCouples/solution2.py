class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # 带路径压缩的并查集，O(n)
        n = len(row) // 2
        root = [i for i in range(n)]
        rank = [1 for i in range(n)]
        ans = 0
        def find(p, root):
            if p != root[p]:
                p = find(root[p], root)
            return root[p]

        def union(x, y, root):
            rootx, rooty = find(x, root), find(y, root)
            if rootx != rooty:
                if rank[rootx] < rank[rooty]:
                    rootx, rooty = rooty, rootx
                root[rooty] = rootx
                if rank[rootx] == rank[rooty]:
                    rank[rootx] += 1
                return 1
            return 0

        for i in range(0, 2*n, 2):
            if row[i]//2 != row[i+1]//2:
                ans += union(row[i]//2, row[i+1]//2, root)
        return ans
