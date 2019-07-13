# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        # If the linked list was empty, there would be 0 components
        if not head:
            return 0
        
        # No components as of now
        ongoing_component = False
        
        # Number of components = 0 initially
        num_components = 0
        
        # Linked list iterator
        list_itr = head
        
        # Convert the list G to a set
        G = set(G)
        
        # Iterate over all the nodes in the linke list
        while list_itr:
            
            # If the node belongs to G
            if list_itr.val in G:
                
                # Increase the number of components if this the start of a new component
                num_components += (ongoing_component == False)
                ongoing_component = True
            else:
                ongoing_component = False
                
            # Move onto the next node    
            list_itr = list_itr.next    
        return num_components         