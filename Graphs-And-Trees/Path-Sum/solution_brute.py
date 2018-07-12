# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.counter = 0
    
    def checkSum(self, root, val, print_val=False):
        if not root:
            return
        new_val = val - root.val
        if new_val == 0:
            self.counter += 1
        self.checkSum(root.left, new_val, print_val)    
        self.checkSum(root.right, new_val, print_val)    
    
    def recurse(self, root, sum):
        if not root:
            return
        self.checkSum(root, sum)
        self.recurse(root.left, sum)
        self.recurse(root.right, sum)
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.recurse(root, sum)
        return self.counter