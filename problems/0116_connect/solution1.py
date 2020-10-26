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
        que = collections.deque()
        if not root: return 
        que.append(root)
        while que:
            sub = collections.deque()
            while que:
                p = que.popleft()
                p.next = que[0] if que else None
                if p.left: sub.extend([p.left, p.right])
            que = sub
        return root
