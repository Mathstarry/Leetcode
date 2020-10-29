# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return []
        que = collections.deque()
        p = head
        while p:
            que.append(p)
            p = p.next
        dummy = ListNode(0)
        q, l = dummy, 0
        while que:
            if l % 2 == 0:
                node = que.popleft()
            else:
                node = que.pop()
            l += 1
            q.next = node
            q = q.next
        q.next = None
