# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        odd = True if not fast else False
        l2 = slow.next
        slow.next = None
        slow, fast = head, head.next
        slow.next = None
        while fast:
            tmp = fast.next
            fast.next = slow
            slow, fast = fast, tmp
        l1 = slow if not odd else slow.next
        while l1:
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next
        return True
