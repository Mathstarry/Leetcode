class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        for t in S:
            if t in J:
                res += 1
        return res
    
