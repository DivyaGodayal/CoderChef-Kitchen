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

        # The variables for running the algorithm
        ongoing_dup = None
        prev, ptr = head, head.next
        final_head, final = None, None

        while ptr:
            # Unique node found, add to the final list
            if prev.val != ptr.val and ongoing_dup is None:
                if not final_head:
                    final_head = prev
                else:
                    final.next = prev
                final = prev
            elif prev.val == ptr.val:
                # Duplication found.
                ongoing_dup = prev.val
            else:
                # Duplication end. Move one step forward
                ongoing_dup = None
            prev.next = None
            prev = ptr
            ptr = ptr.next

        # Edge case handling when last node was unique
        if ongoing_dup is None:
            if not final_head:
                return prev
            final.next = prev
        return final_head
