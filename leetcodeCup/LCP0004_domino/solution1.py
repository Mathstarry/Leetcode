class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        # edges 记录每个格子所匹配的格子，None表示未匹配，#表示坏掉的格子
        edges = [[None] * m for _ in range(n)]
        for x, y in broken:
            edges[x][y] = "#"
        
        def neig(x, y):
            for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                if 0<= nx < n and 0 <= ny < m:
                    yield nx, ny

        def hungariam(x, y, vst):
            vst.add((x, y))
            # 每个格子要递归地搜索其相邻的四个格子，但不会查已搜索过的，所以最差是搜索全部的格子, O(n^2)
            for nx, ny in neig(x, y):
                # nxy 为相邻格子已匹配的格子（可以是None）
                nxy = edges[nx][ny]
                # 如果该点已经在增广路径上，则不用这个点
                if nxy in vst:
                    continue
                # 若 nxy 为 None，则该格子尚未匹配，否则寻找其增广路径
                if not nxy or hungariam(*nxy, vst):
                    edges[x][y] = (nx, ny)
                    edges[nx][ny] = (x, y)
                    # 如果最终寻找到一条增广路径，即最后能找到一个多余的空格子进行匹配，返回 True
                    return True
            # 找不到增广路径
            return False


        # 每条边只有2个顶点，每个顶点只有一条边，所以求出所有已匹配的奇数点个数即可
        res = 0
        for i in range(n):
            for j in range(m):
                # 要遍历 O(n^2) 个格子，只搜索未匹配的格子
                if (i + j) % 2 == 1 and not edges[i][j] and edges[i][j] != "#":
                    out = hungariam(i, j, {"#"})
                    if out: res += 1
        return res
