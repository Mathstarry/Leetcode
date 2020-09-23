class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        # dct 记录每个数字的频率，freq记录每种频率的数字数
        dct, freq, ans = {}, {}, 1
        for i, v in enumerate(nums):
            dct[v] = dct.get(v, 0) + 1
            freq[dct[v]] = freq.get(dct[v], 0) + 1
            if dct[v] > 1:
                freq[dct[v] - 1] -= 1
                if freq[dct[v] - 1] == 0:
                    freq.pop(dct[v] - 1)
            
            # 1. freq 中频率为 1 的数字只有 1 个，其余数字频率均相同
            # 2. freq 中只有两种频率，最大频率比最小频率大 1，且最大频率的数字只有 1 个
            # 3. freq 中只有频率 1
            # 4. freq 中只有 1 种数字
            if len(freq) == 2:
                x, y = min(freq.keys()), max(freq.keys())
                if (x == 1 and freq[x] == 1) or (y == x + 1 and freq[y] == 1):
                    ans = i + 1
            elif len(freq) == 1:
                # 这里若不加逗号，则是将字典中键值对的索引赋给左边，会报错，加逗号，则表示把该键值对的值赋给等号左边
                (x, y), = freq.items()
                if x == 1 or y == 1:
                    ans = i + 1
        return ans
