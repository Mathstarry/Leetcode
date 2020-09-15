class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        ans = 0
        for i in range(0, len(row), 2):
            # 若row[i]为偶数，则row[i]^1 = row[i] + 1, 否则，row[i]^1 = row[i] - 1,正好符合题意
            if row[i + 1] == row[i] ^ 1: continue
            for j in range(i + 2, len(row)):
                if row[j] == row[i] ^ 1:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    break
            ans += 1
        return ans
