class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        m = len(beginWord)
        if endWord not in wordList: return []
        # 相邻字符匹配模板
        dct = collections.defaultdict(list)
        for word in wordList:
            for i in range(m):
                dct[word[:i] + "*" + word[i+1:]].append(word)

        # 相邻字符转换函数
        def change(word):
            for i in range(m):
                tem = word[:i] + "*" + word[i+1:]
                for t in dct[tem]:
                    if t not in vst:
                        yield t

        stack, vst, res = [[beginWord]], {beginWord}, []
        while stack:
            sub, flag = [], False
            for path in stack:
                for t in change(path[-1]):
                    if t not in vst:
                        v = path + [t]
                        sub.append(v)
                        if t == endWord:
                            res.append(v)
                            flag = True
            stack = sub
            for tail in sub:
                vst.add(tail[-1])
            if flag: break
        return res
