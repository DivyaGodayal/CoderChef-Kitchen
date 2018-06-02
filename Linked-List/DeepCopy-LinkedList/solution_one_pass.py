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
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        visited = {}
        old_node = head 
        # Creating the new head node.       
        new_node = RandomListNode(old_node.label)
        visited[old_node] = new_node
        while old_node != None:
            # If the random node exists then 
            if old_node.random:
                # Check if its in the visited dictionary          
                if old_node.random in visited:
                    # If its in the visited dictionary then return the new node reference from the dictionary
                    new_node.random = visited[old_node.random]
                else:
                    # Otherwise create a new node and save it in the visited dictionary
                    new_node.random = RandomListNode(old_node.random.label)
                    visited[old_node.random] = new_node.random
            
            # If the next node exists then
            if old_node.next:
                 # Check if its in the visited dictionary
                if old_node.next in visited:
                    # If its in the visited dictionary then return the new node reference from the dictionary
                    new_node.next = visited[old_node.next]
                else:
                    # Otherwise create a new node and save it in the visited dictionary
                    new_node.next = RandomListNode(old_node.next.label)
                    visited[old_node.next] = new_node.next
            
            # Move the old node and new node reference to the next pointer.
            old_node = old_node.next
            new_node = new_node.next 
            
        return visited[head]
            
            
