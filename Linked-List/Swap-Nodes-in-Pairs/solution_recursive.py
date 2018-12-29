# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If the list has ended or has one node.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        firstNode = head
        secondNode = head.next

        # Swapping
        firstNode.next  = self.swapPairs(secondNode.next)
        secondNode.next = firstNode

        return secondNode
