# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        if len(postorder)==0:
            return None
        
        value = postorder[-1]
        rootNode = TreeNode(value)
        
        index = inorder.index(value)
        
        rootNode.left = self.buildTree(inorder[:index],postorder[0:index])
        rootNode.right = self.buildTree(inorder[index+1:],postorder[index:-1])
        
        return rootNode
        