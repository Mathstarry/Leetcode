class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph, edges = {}, set()
        for u, v in roads:
            graph[u] = graph.get(u, 0) + 1
            graph[v] = graph.get(v, 0) + 1
            edges.add((u, v))
            edges.add((v, u))
        res = 0
        for i in range(n-1):
            for j in range(i+1, n):
                cur = -1 if (i, j) in edges else 0
                if i in graph: cur += graph[i]
                if j in graph: cur += graph[j]
                res = max(res, cur)
        return res
