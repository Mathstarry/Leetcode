"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return 
        stack = [root, "#"]
        while stack:
            node = stack.pop(0)
            if node == "#":
                if stack:
                    stack.append("#")
                    continue
                else:
                    break
            node.next = stack[0] if stack and stack[0] != "#" else None
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return root
