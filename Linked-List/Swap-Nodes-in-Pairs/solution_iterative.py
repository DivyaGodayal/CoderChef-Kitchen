class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Empty list
        if not head:
            return head

        # Initializing the first node of swap
        firstNode = head

        # previous node
        prevNode = head

        # Saving the node to be returned
        # Since the linked list structure would change.
        returnNode = head.next

        while firstNode and firstNode.next:

            # Second node of swap
            secondNode = firstNode.next

            # Swapping
            prevNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode

            # Reinitializing the firstNode and prevNode for next swap
            prevNode = firstNode
            firstNode = firstNode.next

        return returnNode if returnNode else head
