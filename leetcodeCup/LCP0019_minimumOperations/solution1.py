class Solution:
    def minimumOperations(self, leaves: str) -> int:
        # a, b, c 分别表示 0, 1, 2 的前缀和
        def isSame(s, color):
            return 1 if s == color else 0

        a = isSame(leaves[0], "y")
        b = c = float("inf")
        for i in range(1, len(leaves)):
            c = min(b, c) + isSame(leaves[i], "y")
            b = min(a, b) + isSame(leaves[i], "r")
            a = a + isSame(leaves[i], "y")
        return c
