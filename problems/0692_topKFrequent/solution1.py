class Solution(object):
    def topKFrequent(self, words, k):
        dct = collections.Counter(words)
        pq = [(-freq, word) for word, freq in dct.items()]
        heapq.heapify(pq)
        return [heapq.heappop(pq)[1] for _ in range(k)]
