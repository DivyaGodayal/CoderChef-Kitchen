class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        # Special case handling. If we need to add a new node at 
        # level 1, no need to do any sort of traversal
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        
        # Helper function for performing depth first traversal
        def recurse(node, depth):
            
            # If we reach the level "d - 1", we add the two new nodes and return
            if depth == d - 1:
                
                # Two new nodes with the value "v" given in the main input
                new_node_left = TreeNode(v)
                new_node_right = TreeNode(v)
                
                # Original left child becomes the left child of newly create left node
                new_node_left.left = node.left
                node.left = new_node_left

                # Original right child becomes the right child of newly create right node
                new_node_right.right = node.right
                node.right = new_node_right
                
                # Don't process any nodes further down
                return
            else:
                
                # If we haven't reached the required depth, keep recursing on the left and 
                # right side and for every recursive call, pass depth one more than the 
                # input value to this helper function
                if node.left:
                    recurse(node.left, depth + 1)
                if node.right:    
                    recurse(node.right, depth + 1)
                
        recurse(root, 1) 
        return root