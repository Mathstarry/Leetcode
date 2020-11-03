# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def recur(prev, root):
            if not root: return 0
            prev = prev*10 + root.val
            if not root.left and not root.right: return prev
            return recur(prev, root.left) + recur(prev, root.right)
        return recur(0, root)
