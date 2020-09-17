class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 3
        N = n * n
        rows = [0] * N
        cols = [0] * N
        boxs = [0] * N

        # 用以给第v位填上 1 或去掉 1
        def adj(x, y, v):
            k = (x//n) * n + (y//n)
            rows[x] ^= 1 << v
            cols[y] ^= 1 << v
            boxs[k] ^= 1 << v

        def recur(num):
            if num == len(blocks):
                self.solved = True
                return
            x, y = blocks[num]
            k = (x//n) * n + (y//n)
            # 获取这一格可以填的所有数字
            mask = ~(rows[x] | cols[y] | boxs[k]) & (2**N - 1)
            while mask:
                # 获取 cand 最低位的 1
                lowbit = mask & (-mask)
                # 将lowbit表示成二进制形式，并通过计算 0 的个数来获取 1 在第几位
                pos = bin(lowbit).count('0') - 1
                # 将倒数第pos位的状态改成 1
                adj(x, y, pos)
                # 在board[x][y]的位置填上 pos+1
                board[x][y] = str(pos + 1)
                # 继续递归下一格空格
                recur(num+1)
                # 将倒数第pos位的状态改回 0
                adj(x, y, pos)
                # 回溯回这一格时，将cand最低位的 1 置为 0
                mask &= (mask - 1)
                if self.solved:
                    return


        blocks = []
        self.solved = False
        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    blocks.append((i, j))
                else:
                    v = int(board[i][j]) - 1
                    adj(i, j, v)                       
        recur(0)

