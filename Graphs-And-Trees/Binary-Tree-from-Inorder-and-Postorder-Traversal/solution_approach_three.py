# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.inorderMap = {}
    
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inOrderMap = {inorder[i]:i for i in range(len(inorder))}
        return self.build(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1)
    
    
    def build(self,inorder,iLeft,iRight,postorder,pLeft,pRight):
        
        
        
        if pLeft>pRight:
            return None
        
        rootVal = postorder[pRight]
        rootNode = TreeNode(rootVal)
        
        index = self.inOrderMap[rootVal]
        
        rootNode.left = self.build(inorder,iLeft,index-1,postorder,pLeft,pLeft+(index-iLeft)-1)
        rootNode.right = self.build(inorder,index+1,iRight,postorder,pLeft+(index-iLeft),pRight-1)
        
        return rootNode
        