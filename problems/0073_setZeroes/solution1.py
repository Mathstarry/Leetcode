class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                matrix[i][j] <<= 1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for t in range(m):
                        if matrix[i][t] != 0 and matrix[i][t] & 1 == 0:
                            matrix[i][t] += 1
                    for s in range(n):
                        if matrix[s][j] != 0 and matrix[s][j] & 1 == 0:
                            matrix[s][j] += 1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] >>= 1
