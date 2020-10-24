# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root, a):
            if not root: return 
            b = inorder(root.left, a)
            if b: a = b
            self.res = min(self.res, root.val - a)
            c = inorder(root.right, root.val)
            return c if c else root.val
        
        self.res = float("inf")
        inorder(root, float("-inf"))
        return self.res
