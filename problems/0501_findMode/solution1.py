# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        lst, res, maxL = [], {}, 0
        def inorder(root):
            if not root: return
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)
        
        inorder(root)
        for t in lst:
            res[t] = res.get(t, 0) + 1
            if res[t] > maxL:
                maxL = res[t]
        ans = []
        for k, v in res.items():
            if v == maxL:
                ans.append(k)
        return ans
