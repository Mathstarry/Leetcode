class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        freq = {chr(t): -1 for t in range(97, 123)}
        for word in A:
            tmp = collections.defaultdict(int)
            for i, v in enumerate(word):
                tmp[v] += 1
            for i in range(97, 123):
                freq[chr(i)] = min(freq[chr(i)], tmp[chr(i)]) if freq[chr(i)] > -1 else tmp[chr(i)]

        res = []
        for i, v in freq.items():
            k = v
            while k > 0:
                res.append(i)
                k -= 1
        return res
