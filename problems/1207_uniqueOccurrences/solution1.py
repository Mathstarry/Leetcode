class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = collections.defaultdict(int)
        for t in arr:
            freq[t] += 1
        appear = set()
        for v in freq.values():
            if v in appear:
                return False
            appear.add(v)
        return True
