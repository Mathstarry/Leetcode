class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        ans = [-1, -1, -1]
        # left 和 upon 分别记录了当前点向左以及向上有多少个连续的 0
        left = [[0] * (n+1) for _ in range(n+1)]
        upon = [0] * (n+1)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == 0:
                    # 由于是按行扫描，我们只需要一行upon，所以可以原地更新
                    left[i][j] = left[i][j-1] + 1
                    upon[j] = upon[j] + 1
                    v = min(left[i][j], upon[j])
                    for k in range(v, ans[2], -1):
                        if upon[j-k+1] >= k and left[i-k+1][j] >= k:
                            ans = [i-k, j-k, k]
                            break
                else:
                    upon[j] = 0
        return ans if ans[2] > 0 else []
