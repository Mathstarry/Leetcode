class Solution:
    def demo(self, n: int, m: int) -> int:
        # 匈牙利算法
        def neig(x, y):
            for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                if 0 <= nx < n and 0 <= ny < m:
                    yield nx, ny

        def hungariam(x, y, vst):
            vst.add((x, y))
            for nx, ny in neig(x, y):
                nxy = edges[nx][ny]
                # 若顶点已在增广路径上，则跳过
                if nxy in vst:
                    continue
                # 如果有可匹配的空闲顶点，则表明找到了一条增广路径，否则继续寻找
                if not nxy or hungariam(*nxy, vst):
                    edges[x][y] = (nx, ny)
                    edges[nx][ny] = (x, y)
                    return True
            return False

        res, vst = 0, set()
        # 建立顶点的匹配，初始化未匹配
        edges = [[None] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if (i + j) % 2 == 1 and not edges[i][j]:
                    # 遍历所有奇数点
                    out = hungariam(i, j, vst)
                    # 记录已匹配的边数
                    if out: res += 1
        return res
