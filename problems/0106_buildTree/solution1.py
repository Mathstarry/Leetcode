# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        dct = {v: i for i, v in enumerate(inorder)}

        def recur(l, r, l2, r2):
            if l > r: return None
            if l == r:
                return TreeNode(inorder[l])
            root = TreeNode(postorder[r2])
            idx = dct[postorder[r2]]

            root.left = recur(l, idx-1, l2, l2+idx-l-1)
            root.right = recur(idx+1, r, l2+idx-l, r2-1)
            return root
        
        return recur(0, len(inorder)-1, 0, len(inorder)-1)
