# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # isUp 表示父结点是否有监控，isCover 表示该结点是否有监控
        @lru_cache(None)
        def recur(root, isUp, isCover):
            if not root: return -1 if isCover else 0
            cl, ncl = recur(root.left, isCover, True) + 1, recur(root.left, isCover, False)
            cr, ncr = recur(root.right, isCover, True) + 1, recur(root.right, isCover, False)
            if not isUp and not isCover:
                if root.left and root.right:
                    return min(cl+cr, cl+ncr, cr+ncl)
                elif root.left:
                    return cl
                elif root.right:
                    return cr
                else:
                    return 1
            else:
                return min(cl+cr, cl+ncr, ncl+cr, ncl+ncr)

        return min(recur(root, False, False), recur(root, False, True) + 1)
