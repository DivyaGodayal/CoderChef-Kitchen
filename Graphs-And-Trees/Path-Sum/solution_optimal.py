# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        # To count the total number of paths
        self.count_paths = 0
        # To keep a track of the running sum of a particular node down the path.
        # Where running sum for any node would be the sum of all node values from root to the current node.
        self.running_sum_dict = {}
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Target sum is the desired sum for the path.
        target_sum = sum
        def recurse_depth(node, running_sum):
        
            if node is None:
                return
            
            running_sum += node.val
            
            # We calculate the the deviation of the current running sum from the target sum.
            deviation = running_sum - target_sum
            
            # if the deviation is present in the running sum dictionary then this means there is a extraneous path
            # Which could be removed to get rid of the deviation and reach the desired target sum 
            if deviation in self.running_sum_dict:
                # if there are multiple subpaths which have the same running sum as needed for the deviation
                # this means each of these removed individually can be used to form the desired path sum.
                self.count_paths += self.running_sum_dict[deviation]
                
            # Adding the current running sum to the dictionary.
            if running_sum not in self.running_sum_dict:
                 self.running_sum_dict[running_sum] = 0
            # We use the value of the dictionary to keep a track of number of subpaths with a given running sum.
            self.running_sum_dict[running_sum] += 1
            
            # Recurse the depth of the tree to explore all path combinations
            recurse_depth(node.left, running_sum)
            recurse_depth(node.right, running_sum)
            self.running_sum_dict[running_sum] -= 1
            
        #Call the recursive depth function on root node
        self.running_sum_dict = {0:1}
        recurse_depth(root, 0)
        
        return self.count_paths
            
                

        
            
        