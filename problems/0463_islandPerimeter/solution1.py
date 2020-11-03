class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        x, y, n, m = -1, -1, len(grid), len(grid[0])
        que = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    x, y = i, j
                    que.append((x, y))
                    break
            if x != -1:
                break
        res, vst = 0, {(x, y)}
        while que:
            i, j = que.popleft()
            cnt = 4
            for xx, yy in [(i, j-1), (i+1, j), (i, j+1), (i-1, j)]:
                if 0 <= xx < n and 0 <= yy < m and grid[xx][yy] == 1:
                    cnt -= 1
                    if (xx, yy) not in vst:
                        que.append((xx, yy))
                        vst.add((xx, yy))
            res += cnt
        return res
