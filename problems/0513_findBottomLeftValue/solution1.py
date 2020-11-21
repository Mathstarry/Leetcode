# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        que = [root]
        while que:
            sub = []
            for node in que:
                if node.left: sub.append(node.left)
                if node.right: sub.append(node.right)
            if not sub:
                return que[0].val
            que = sub
