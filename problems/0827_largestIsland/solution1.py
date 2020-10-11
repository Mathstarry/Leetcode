class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def neig(i, j):
            for x, y in [(i + 1, j), (i, j - 1), (i - 1, j), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < m:
                    yield x, y

        def dfs(i, j, k):
            grid[i][j] = k
            res = 1
            for x, y in neig(i, j):
                if grid[x][y] == 1:
                    res += dfs(x, y, k)
            return res

        dct, hasZero, res = {0: 0}, False, 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dct[i*m + j + 2] = dfs(i, j, i*m + j + 2)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    hasZero = True
                    cnt, vst = 1, set()
                    for x, y in neig(i, j):
                        if grid[x][y] not in vst:
                            cnt += dct[grid[x][y]]
                            vst.add(grid[x][y])
                    res = max(res, cnt)
        return res if hasZero else n * m
