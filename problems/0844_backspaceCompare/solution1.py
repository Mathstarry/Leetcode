class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackA, stackB = [], []
        for t in S:
            if t == "#":
                if stackA:
                    stackA.pop()
            else:
                stackA.append(t)
        for t in T:
            if t == "#":
                if stackB:
                    stackB.pop()
            else:
                stackB.append(t)
        return stackA == stackB
