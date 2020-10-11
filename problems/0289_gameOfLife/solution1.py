class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def neig(x, y):
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if not (i==x and j==y) and 0 <= i < n and 0 <= j < m:
                        yield i, j

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                cnt = 0
                for dx, dy in neig(i, j):
                    # 最低位存储当前状态
                    cnt += board[dx][dy] & 1
                if cnt == 3 or (cnt == 2 and board[i][j] == 1):
                    # 第二低位存储下一状态
                    board[i][j] += 2
        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1
