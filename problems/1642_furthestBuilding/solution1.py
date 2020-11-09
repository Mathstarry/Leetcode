class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n, rest = ladders, bricks
        pq, res = [], 0
        dct = {len(heights) - 1: 0}
        for i in range(len(heights) - 1):
            if heights[i + 1] - heights[i] > 0:
                dct[i] = heights[i + 1] - heights[i]
        for k in sorted(dct.keys()):
            v, cur = dct[k], 0
            heapq.heappush(pq, v)
            if len(pq) > n:
                cur = heapq.heappop(pq)
            rest -= cur
            res = k
            if rest < 0:
                break
        return res
