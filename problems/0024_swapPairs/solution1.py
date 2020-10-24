# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy.next
        while fast and fast.next:
            tmp = fast.next
            slow.next = tmp
            fast.next = tmp.next
            tmp.next = fast
            slow, fast = fast, fast.next
        return dummy.next
