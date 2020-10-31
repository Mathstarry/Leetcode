# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p, tmp, dct = dummy, 0, {}
        while p:
            tmp += p.val
            dct[tmp] = p
            p = p.next
        
        p, tmp = dummy, 0
        while p:
            tmp += p.val
            p.next = dct[tmp].next
            p = p.next
        return dummy.next
