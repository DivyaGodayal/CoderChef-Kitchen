# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head:
            return head

        # dictionary to hold the old node as key and corresponding copied node as value    
        dicti = {None: None}
        
        ptr = head
        prev = None
        new_head = None
        # Creating a copy of linked list which traverses the next pointers.
        # The new linked list has just the values and next pointers from the old linked list.
        # Saving the corresponding new nodes in the dictionary to be used later.
        while ptr:
            new_node = RandomListNode(ptr.label)
            if not new_head:
                new_head = new_node
            dicti[ptr] = new_node
            if prev:
                prev.next = new_node
            ptr = ptr.next
            prev = new_node
            
        ptr = head
        new_ptr = new_head
        # Since the random pointers are random and can point to any of the nodes in the above linkedlist.
        # Hence copying random pointers is second step, once we have new nodes in the dicitonary.
        # Now add the random pointers to the nodes in the new linkedlist, by getting corresponding new nodes from dictionary.
        while ptr:
            new_ptr.random = dicti[ptr.random]
            ptr = ptr.next
            new_ptr = new_ptr.next
            
        return new_head 