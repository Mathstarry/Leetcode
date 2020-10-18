# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        slow, fast = head, head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast == slow: return True
            if not fast: return False
            fast = fast.next
            if fast == slow: return True
        return False
