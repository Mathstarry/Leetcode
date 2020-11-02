"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def recur(cur):
            if not cur.next and not cur.child: return cur
            if not cur.child:
                return recur(cur.next)
            else:
                nt = cur.next
                tmp = cur.child
                cur.child = None
                cur.next, tmp.prev = tmp, cur
                cur = recur(tmp)
                if nt:
                    cur.next, nt.prev = nt, cur
                    return recur(nt)
                else:
                    return cur

        if not head: return 
        dummy = Node(0)
        dummy.next = head
        recur(head)
        return dummy.next
