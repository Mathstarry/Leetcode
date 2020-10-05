# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        stack, level = [root], 0
        while stack:
            sub = []
            pre = 0 if level % 2 == 0 else float("inf")
            coef = 1 if level % 2 == 0 else -1
            odd = 1 if level % 2 == 0 else 0
            for node in stack:
                if pre*coef >= node.val*coef or node.val % 2 != odd:
                    return False
                pre = node.val
                if node.left: sub.append(node.left)
                if node.right: sub.append(node.right)
            stack = sub
            level += 1
        return True
            
        
