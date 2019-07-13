# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        # Base case where the tree is empty
        if not root:
            return []
        
        # Initialize the queue with the root node
        # This is the level-0
        Q = [root]
        max_per_level = []
        
        # Iterate until the queue becomes empty
        while Q:
            
            # Number of elements in the current level
            num_elements_current_level = len(Q)
            
            # Resetting the level maximum to the first node's value in the current level
            level_max = Q[0].val
            
            # Iterate over all the elements in the current level
            for _ in range(num_elements_current_level):
                element = Q.pop(0)
                
                # Update the level maximum
                level_max = max(level_max, element.val)
                
                # Push the left child into the queue if one exists
                if element.left:
                    Q.append(element.left)
                    
                # Push the right child into the queue if one exists    
                if element.right:
                    Q.append(element.right)
            
            # Append the maximum element to the array we have to return
            max_per_level.append(level_max)    
        return max_per_level      