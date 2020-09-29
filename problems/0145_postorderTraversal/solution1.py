# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def recur(root):
            if not root: return
            recur(root.left)
            recur(root.right)
            self.res.append(root.val)

        self.res = []
        recur(root)
        return self.res
