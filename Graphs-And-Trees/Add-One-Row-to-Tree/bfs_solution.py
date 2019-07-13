class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        # Special case handling. If we need to add a new node at 
        # level 1, no need to do any sort of traversal
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        
        # Level of the root node is 1
        # The queue initially contains the root node only
        level = 1
        Q = [root]
        
        # We only process nodes till we reach the level d - 1
        while level < d - 1:
            
            # Note the size of the queue. This is the number of nodes at "level"
            size = len(Q)
            
            # Process all these nodes at this "level"
            for _ in range(size):
                element = Q.pop(0)
                
                # Add the left child to the queue if any
                if element.left:
                    Q.append(element.left)
                
                # Add the right child to the queue if any
                if element.right:
                    Q.append(element.right) 
                    
            # Increment the level since all the nodes of the next level are now in the queue        
            level += 1        
        
        # Once out of the previous "while" loop, we will have all the nodes at 
        # depth "d - 1". For each node we add two new nodes
        while Q:
            node = Q.pop(0)
            new_left = TreeNode(v)
            new_right = TreeNode(v)
            
            new_left.left = node.left
            new_right.right = node.right
            
            node.left = new_left
            node.right = new_right
        
        return root