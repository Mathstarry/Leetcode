# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root: return 0
            l = dfs(root.left)
            if l == -1: return -1
            r = dfs(root.right)
            if r == -1: return -1
            return max(l, r) + 1 if abs(l - r) < 2 else -1
        return False if dfs(root) == -1 else True
