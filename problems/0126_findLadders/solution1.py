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
        res, flag, isOne = [], False, True
        stack, stack2 = [[beginWord]], [[endWord]]
        vst, vst2 = {beginWord}, {endWord} 
        while stack and not flag:
            if len(stack[0]) > len(stack2[0]):
                stack, stack2 = stack2, stack
                vst, vst2 = vst2, vst
                isOne = not isOne
            sub = []
            k = -1 if isOne else 0
            for word in stack:
                for t in change(word[k]):
                    if t not in vst:
                        v = word + [t] if isOne else [t] + word
                        sub.append(v)
                        if t in vst2:
                            flag = True
                            for s in stack2:
                                if s[-1 - k] == t:
                                    tmp = v + s[1:] if isOne else s + v[1:]
                                    res.append(tmp)
            for word in sub:
                vst.add(word[k])
            stack = sub
        return res
