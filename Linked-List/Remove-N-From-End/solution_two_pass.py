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

        # Pass 1 to find the length of the list
        ptr = head
        length = 0
        while ptr:
            length += 1
            ptr = ptr.next

        # Pass 2 to delete the required node
        prev, ptr = None, head
        i = 0
        while i < (length - n):
            i += 1
            prev = ptr
            ptr = ptr.next

        # Edge case handling when the first node of the linked list is to be deleted
        if not prev:
            head = head.next
        else:
            prev.next = ptr.next

        return head
