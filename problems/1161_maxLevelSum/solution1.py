# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root: return 0
        maxV, best, level = root.val, 1, 1
        stack = [root]
        while stack:
            sub = []
            for node in stack:
                if node.left: sub.append(node.left)
                if node.right: sub.append(node.right)
            stack = sub
            level += 1
            v = sum([t.val for t in sub])
            if sub and v > maxV:
                maxV, best = v, level
        return best
