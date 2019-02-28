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
    
    private:
    map<int, int> inOrderMap; 
    
    public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        
        for(int i=0;i<inorder.size();++i){
            this->inOrderMap[inorder[i]]=i;
        }
        return this->build(inorder,0,inorder.size()-1,postorder,0,postorder.size()-1);
    }
    
    TreeNode* build(vector<int>& inorder,int iLeft,int iRight,vector<int>& postorder,int pLeft,int pRight){
        
        if(pLeft>pRight){
            return NULL;
        }
        
        int rootVal = postorder[pRight];
        TreeNode* root = new TreeNode(rootVal);
        
        int indexInInorder = this->inOrderMap.find(rootVal)->second;
        
        root->left = this->build(inorder,iLeft,indexInInorder-1,postorder,pLeft,pLeft+(indexInInorder-iLeft)-1);
        root->right = this->build(inorder,indexInInorder+1,iRight,postorder,pLeft+(indexInInorder-iLeft),pRight-1);
        
        return root;
        
    }
    
};