class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return 
        def recur(root, p):
            if root.left: 
                p.right = TreeNode(root.left.val)
                recur(root.left, p.right)

            if root.right: 
                p.left = TreeNode(root.right.val)
                recur(root.right, p.left)

        dummy = TreeNode(root.val)
        recur(root, dummy)
        return dummy
