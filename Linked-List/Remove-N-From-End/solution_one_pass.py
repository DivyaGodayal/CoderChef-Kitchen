# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # Move ptr2 N steps forward
        ptr1, ptr2 = head, head
        while n > 0:
            ptr2 = ptr2.next
            n -= 1

        # Move both pointers one step at a time
        prev = None
        while ptr2:
            prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if prev:
            prev.next = ptr1.next
        else:
            head = head.next

        return head    
