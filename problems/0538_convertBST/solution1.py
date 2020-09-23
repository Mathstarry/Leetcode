# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def recur(root, num):
            if not root: return num
            root.val += recur(root.right, num)
            return recur(root.left, root.val) 
            
        recur(root, 0)
        return root
