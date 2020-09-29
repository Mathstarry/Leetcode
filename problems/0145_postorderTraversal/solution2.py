# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return 
        stack, cur, res = [], root, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.right:
                tmp = TreeNode(cur.val)
                stack.append(tmp)
            else:
                res.append(cur.val)
            cur = cur.right

        return res
