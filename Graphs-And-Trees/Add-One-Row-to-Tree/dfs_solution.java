class Solution {
    
    int lvl, value;
    
    // Helper function for performing depth first traversal
    private void recurse(TreeNode node, int depth) {
        
        // If we reach the level "d - 1", we add the two new nodes and return
        if (depth == this.lvl - 1) {
            
            // Two new nodes with the value "v" given in the main input
            TreeNode newNodeLeft = new TreeNode(this.value);
            TreeNode newNodeRight = new TreeNode(this.value);

            // Original left child becomes the left child of newly create left node
            newNodeLeft.left = node.left;
            node.left = newNodeLeft;

            // Original right child becomes the right child of newly create right node
            newNodeRight.right = node.right;
            node.right = newNodeRight;

            // Don't process any nodes further down
            return;
        } else {
            
            // If we haven't reached the required depth, keep recursing on the left and 
            // right side and for every recursive call, pass depth one more than the 
            // input value to this helper function
            if (node.left != null) {
                recurse(node.left, depth + 1);
            }
                
            if (node.right != null) {
                recurse(node.right, depth + 1);
            }
                
        }
    }
    
    public TreeNode addOneRow(TreeNode root, int v, int d) {
        
        // Special case handling. If we need to add a new node at 
        // level 1, no need to do any sort of traversal
        if (d == 1) {
            TreeNode new_node = new TreeNode(v);
            new_node.left = root;
            return new_node;
        }
        
        this.lvl = d;
        this.value = v;
        this.recurse(root, 1);
        return root;
            
    }
}