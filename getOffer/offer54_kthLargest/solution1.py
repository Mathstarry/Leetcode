# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack, p = [], root
        while p or stack:
            while p:
                stack.append(p)
                p = p.right
            p = stack.pop()
            k -= 1
            if k == 0: return p.val
            p = p.left
