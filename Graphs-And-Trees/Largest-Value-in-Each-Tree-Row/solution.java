/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> largestValues(TreeNode root) {

        // Base case where the tree is empty
        if (root == null) {
            return new LinkedList<Integer>();
        }

        // Initialize the queue with the root node
        // This is the level-0
        Queue<TreeNode> Q = new LinkedList<TreeNode>();
        Q.add(root);

        List<Integer> maxPerLevel = new LinkedList<Integer>();
        int levelMax = -1;
        TreeNode currentNode;

        // Iterate until the queue becomes empty
        while (Q.size() > 0) {

            // Number of elements in the current level
            int numElementsCurrentLevel = Q.size();

            // Resetting the level maximum to the first node's value in the current level
            levelMax = Q.peek().val;

            // Iterate over all the elements in the current level
            for (int i = 0; i < numElementsCurrentLevel; i++) {
                currentNode = Q.remove();

                // Update the level maximum
                levelMax = Math.max(levelMax, currentNode.val);

                // Push the left child into the queue if one exists
                if (currentNode.left != null) {
                    Q.add(currentNode.left);
                }

                // Push the right child into the queue if one exists    
                if (currentNode.right != null) {
                    Q.add(currentNode.right);
                }
            }

            // Append the maximum element to the array we have to return
            maxPerLevel.add(levelMax);
        }

        return maxPerLevel;
    }
}