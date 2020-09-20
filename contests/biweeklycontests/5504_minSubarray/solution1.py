class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n, summ = len(nums), sum(nums)
        q, r = summ // p, summ % p
        if q == 0: return -1
        if r == 0: return 0
        bestL = n

        # s[i]表示前i-1部分和, s[i] - s[j] = sum(nums[j:i])
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + nums[i]
            s[i + 1] %= p
        # 用字典记录前 i 部分和模 P 同余的几项对应的索引
        dct = {}
        for i, v in enumerate(s):
            dct[v] = dct.get(v, []) + [i]
        # 寻找最小的 abs(i-j) 使得 s[i] - s[j] == r, where i > j
        for i in range(n, -1, -1):
            k = (s[i] - r) % p
            if k in dct:
                for t in dct[k][::-1]:
                    if t < i:
                        bestL = min(bestL, i - t)
                        break

        return bestL if bestL < n else -1
