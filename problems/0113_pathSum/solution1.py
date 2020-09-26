# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def recur(root, s, v):
            if not root:
                return
            val = root.val
            if not root.left and not root.right:
                if v - val == 0:
                    self.res.append(s + [val])
                return
            recur(root.left, s + [val], v - val)
            recur(root.right, s + [val], v - val)
        self.res = []
        recur(root, [], sum)
        return self.res
