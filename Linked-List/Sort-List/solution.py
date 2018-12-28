class Solution(object):
    dummy = ListNode(0)

    # Function to find the middle element of the list
    # Uses the slow-fast pointer approach
    def findMid(self, head):
        prev = None
        slowPtr = head
        fastPtr = head
        while fastPtr and fastPtr.next:
            prev = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        prev.next = None
        return slowPtr

    # Function to merge two sorted linked lists together into one.
    # Makes use of the two-finger approach. Uses a dummy node so as to
    # avoid multiple if-else checks.
    def merge(self, head1, head2):
        final_head = Solution.dummy
        final = final_head
        while head1 and head2:
            if head1.val < head2.val:
                final.next = head1
                final = head1
                head1 = head1.next
            else:
                final.next = head2
                final = head2
                head2 = head2.next

        # Attach the remaining portion of the longer list to the final list
        if head1:
            final.next = head1
        else:
            final.next = head2
        final_head = final_head.next
        return final_head

    def mergeSort(self, head):
        # Base case when the list is empty or just contains one element
        if not head or not head.next: return head

        # Find the middle element and disconnect the list at that node
        mid = self.findMid(head)

        # Sort the two halves recursively
        head1 = self.mergeSort(head)
        head2 = self.mergeSort(mid)

        # Merge them together and return the head of the merged list
        return self.merge(head1, head2)

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)
