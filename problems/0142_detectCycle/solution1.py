# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return 
        slow, fast = head, head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast: return 
            fast = fast.next
            if fast == slow: break
        if not fast: return 
        slow, fast = head, fast.next
        while True:
            if slow == fast: return fast
            slow, fast = slow.next, fast.next
            
