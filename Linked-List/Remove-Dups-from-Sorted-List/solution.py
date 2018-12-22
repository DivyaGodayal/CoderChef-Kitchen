# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Base case when there's just one element or NO elements in the linked list.
        if not head or not head.next:
            return head

        # The two pointers and the prev variable
        ptr = head.next
        prev = head.val
        prev_ptr = head

        while ptr:
            # Duplicate found, delete it
            if ptr.val == prev:
                prev_ptr.next = ptr.next
            else:
                # New value started in the sorted order. Update "prev"
                prev = ptr.val
                prev_ptr = ptr

            # Move one step forward
            ptr = ptr.next

        return head
