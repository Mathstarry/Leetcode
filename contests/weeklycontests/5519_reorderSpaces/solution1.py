class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        cnt = 0
        # 统计空格数量
        for i in range(n):
            if text[i] == ' ':
                cnt += 1
        a = text.split()
        m = len(a) - 1
        # 若只有一个单词，则将空格全放末尾
        if m == 0:
            return a[0] + " " * cnt
        # 否则，将空格平均地放在单词之间，不能被整除的部分放在末尾
        q, r = cnt // m, cnt % m
        b = " " * q
        s = b.join(a) + " " * r
        return s
