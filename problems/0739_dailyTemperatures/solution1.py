class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                t = stack.pop()
                T[t] = i - t
            stack.append(i)
        for t in stack:
            T[t] = 0
        return T
