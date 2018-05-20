/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* preOrderNodeTraversal(TreeNode* node){
        //node is the current node.
        
        //base case
        //if the node is NULL. Either reached the end of branch or tree is empty
        if(node == NULL)
            return NULL;
        
        //creating a pointer for tail Node.
        //where the insertions to right are performed.
        TreeNode* tailNode = node;
        //saving the pointer of right child.
        TreeNode* nodeRight = node->right;
        //since the pointer is saved now, make the right child of current node null
        node->right = NULL;
        
        if(node->left != NULL){
            
            //making recursive call on the left node
            //this would return a flattened binary tree on left node
            //make this as the tailNode now
            //and attach it to the right of current node
            tailNode = preOrderNodeTraversal(node->left);
            //now that the left pointer is saved in tailnode.
            //we can make the left of current node null
            node->left = NULL; 
            //attach the tail node we got to the right of the current node
            node->right = tailNode;        
        }
        
    
        if(nodeRight != NULL){ 
            //making recursive call on the right node
            //this would return a flattened binary tree on right node
            preOrderNodeTraversal(nodeRight);
            //iterate to the leaf node of the flattened binary tree
            //attach the right child of the current node at the end
            while(tailNode != NULL && tailNode->right != NULL)
                tailNode = tailNode->right;
            //attaching the right child
            tailNode->right = nodeRight;
        }    
        return node;
    }
    
    void flatten(TreeNode* root) {
        preOrderNodeTraversal(root);
    }
};
