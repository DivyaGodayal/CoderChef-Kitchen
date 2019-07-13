class Solution {
    
    public TreeNode addOneRow(TreeNode root, int v, int d) {
        
        // Special case handling. If we need to add a new node at 
        // level 1, no need to do any sort of traversal
        if (d == 1) {
            TreeNode new_node = new TreeNode(v);
            new_node.left = root;
            return new_node;
        }
        
        // Level of the root node is 1
        // The queue initially contains the root node only
        int level = 1;
        Queue<TreeNode> Q = new LinkedList<TreeNode>();
        Q.add(root);
        
        // We only process nodes till we reach the level d - 1
        while (level < d - 1) {
            
            // Note the size of the queue. This is the number of nodes at "level"
            int size = Q.size();
            
            // Process all these nodes at this "level"
            for(int i = 0; i < size; i++) {
                
                TreeNode element = Q.remove();
                
                // Add the left child to the queue if any
                if (element.left != null) {
                    Q.add(element.left);
                }
                
                // Add the right child to the queue if any
                if (element.right != null) {
                    Q.add(element.right);
                }
            }
                
            // Increment the level since all the nodes of the next level are now in the queue        
            level++;
        }
            
            
        // Once out of the previous "while" loop, we will have all the nodes at 
        // depth "d - 1". For each node we add two new nodes
        while (Q.size() > 0) {
            TreeNode node = Q.remove();
            
            // Two new nodes with the value "v" given in the main input
            TreeNode newNodeLeft = new TreeNode(v);
            TreeNode newNodeRight = new TreeNode(v);

            // Original left child becomes the left child of newly create left node
            newNodeLeft.left = node.left;
            node.left = newNodeLeft;

            // Original right child becomes the right child of newly create right node
            newNodeRight.right = node.right;
            node.right = newNodeRight;
        }
            
        
        return root;            
    }
}