class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def isOver(x, y):
            a, b = list(map(int, (x.split(":"))))
            c, d = list(map(int, (y.split(":"))))
            if a == c or (c == a + 1 and 60 - b + d <= 60):
                return True
            return False
        
        dct, res = {}, []
        for i in range(len(keyName)):
            dct[keyName[i]] = dct.get(keyName[i], []) + [keyTime[i]]
        for k, v in dct.items():
            if len(v) >= 3:
                v.sort()
                for i in range(len(v)-2):
                    if isOver(v[i], v[i+2]):
                        res.append(k)
                        break
        res.sort()
        return res
