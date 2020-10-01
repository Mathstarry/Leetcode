# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        p = root
        while p:
            if p.val < val:
                if p.right:
                    p = p.right
                else:
                    p.right = TreeNode(val)
                    break
            if p.val > val:
                if p.left:
                    p = p.left
                else:
                    p.left = TreeNode(val)
                    break
        if not root: root = TreeNode(val)
        return root
