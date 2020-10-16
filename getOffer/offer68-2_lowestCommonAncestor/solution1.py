# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recur(root):
            if not root: return False
            m = True if root.val == p.val or root.val == q.val else False
            l = recur(root.left)
            r = recur(root.right)
            if sum([l, m, r]) > 1: self.res = root
            return True if l or r or m else False
        self.res = None
        recur(root)
        return self.res
