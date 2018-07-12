# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        parent = {}
        # Function to fix the parents of all the nodes in the tree. This is simple tree traversal.
        def fix_parents(root):
            if not root:
                return
            
            if root.left:
                parent[root.left] = root
            if root.right:
                parent[root.right] = root
                
            fix_parents(root.left)    
            fix_parents(root.right)    
            
        fix_parents(root) 
        
        # Now we do the level order traversal starting from the target node. 
        visited = {}
        
        # Insert the node and 0 as the starting level
        queue = [(target, 0)]
        
        # We need the visited node so that we don't process same nodes again and again.
        visited[target] = 1
        
        # Final array that we will return
        nodes_at_level_K = []
        
        # While queue is not empty
        while queue:
            element, level = queue.pop(0)
            
            # if the level of the current element is K, then add it to our answer list, else if
            # level > K, then return the array. 
            if level == K:
                nodes_at_level_K.append(element.val)
            elif level == K + 1:
                return nodes_at_level_K
            
            # Individual None, visited checks for left child, right child and parent node. 
            if element.left and element.left not in visited:
                visited[element.left] = 1
                queue.append((element.left, level + 1))
            if element.right and element.right not in visited:
                visited[element.right] = 1
                queue.append((element.right, level + 1))    
            if element in parent and parent[element] not in visited:
                visited[parent[element]] = 1
                queue.append((parent[element], level + 1))
        return nodes_at_level_K         
            
