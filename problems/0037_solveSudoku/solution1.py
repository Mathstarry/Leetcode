class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 3
        N = n * n
        rows = [collections.defaultdict(int) for _ in range(N)]
        cols = [collections.defaultdict(int) for _ in range(N)]
        boxs = [collections.defaultdict(int) for _ in range(N)]

        # 数独初始化
        for i in range(N):
            for j in range(N):
                k = (i//n) * n + (j//n)
                if board[i][j] != '.':
                    v = int(board[i][j])
                    rows[i][v] = cols[j][v] = boxs[k][v] = 1

        def trackback(board, rows, cols, boxs, num):
            # 若 num == N**2，则表示已填完最后一格的数字，数独已解
            if num == N**2:
                self.solved = True
                return

            x, y = num // N, num % N
            # 若当前格已有数字，则填下一格
            if board[x][y] != '.':
                trackback(board, rows, cols, boxs, num + 1)

            # 若当前格无数字填充，则在1～9中寻找满足要求的数字
            else:
                k = (x // n) * n + (y // n)
                for t in range(1, N+1):
                    if rows[x][t] == cols[y][t] == boxs[k][t] == 0:
                        board[x][y] = str(t)
                        rows[x][t] = cols[y][t] = boxs[k][t] = 1
                        trackback(board, rows, cols, boxs, num+1)
                        # 若数独已解，则返回时不需要再把已填的数字消去
                        if not self.solved:
                            board[x][y] = '.'
                            rows[x][t] = cols[y][t] = boxs[k][t] = 0

        self.solved = False
        trackback(board, rows, cols, boxs, 0)
