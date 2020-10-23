class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        towers.sort()
        xbound = towers[-1][0] + radius
        towers.sort(key=lambda x: x[1])
        ybound = towers[-1][1] + radius
        res, ans = 0, [0, 0]
        for x in range(xbound+1):
            for y in range(ybound+1):
                cnt = 0
                for i, j, q in towers:
                    d = math.sqrt(abs(x-i)**2 + abs(y-j)**2)
                    if d <= radius:
                        cnt += q // (1 + d)
                if cnt > res:
                    res = cnt
                    ans = [x, y]
        return ans
        
