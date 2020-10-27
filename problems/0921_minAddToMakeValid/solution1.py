class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        cnt, stack = 0, []
        for t in S:
            if t == "(":
                stack.append(t)
            elif t == ")":
                if not stack:
                    cnt += 1
                else:
                    stack.pop()
        cnt += len(stack)
        return cnt
