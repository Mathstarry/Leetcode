class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        div, res = target // 2, []
        for i in range(div, 1, -1):
            if i % 2 == 1 and target % i == 0 and target//i > (i - 1)//2:
                q, r = target // i, (i - 1) // 2
                res.append([k for k in range(q-r, q+r+1)])
            elif i % 2 == 0 and (target - i//2) % i == 0 and (target - i//2) // i >= i//2:
                r = i // 2
                q = (target - r) // i
                res.append([k for k in range(q-r+1, q+r+1)])
        return res
