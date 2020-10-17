# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy, c = ListNode(0), 0
        cur = dummy
        while l1 or l2 or c:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            cur.next = ListNode((a + b + c) % 10)
            c = (a + b + c) // 10
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next
