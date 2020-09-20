# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root, dirs):
            if not root: return 0
            if not root.left and not root.right:
                return root.val if dirs == "left" else 0
            return dfs(root.left, "left") + dfs(root.right, "right")
        
        if not root: return 0
        return dfs(root.left, "left") + dfs(root.right, "right")
