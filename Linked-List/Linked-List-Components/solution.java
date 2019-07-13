/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int numComponents(ListNode head, int[] G) {

        // Base case
        if (head == null) {
            return 0;
        }

        // Convert the list G to a hash map for better runtime
        HashMap<Integer, Integer> G_hash = new HashMap<Integer, Integer>();
        for (int i = 0; i < G.length; i++) {
            G_hash.put(G[i], 1);
        }

        // Components counter
        int numComponents = 0;

        // Keeping track of an ongoing component
        boolean ongoingComponent = false;

        // Linked list iterator
        ListNode listIter = head;
        while (listIter != null) {

            // If the Hash contains the node
            if (G_hash.containsKey(listIter.val)) {

                // Increment the number of components if this is the 
                // starting point of a new component
                numComponents += (ongoingComponent == false ? 1 : 0);
                ongoingComponent = true;
            } else {

                // Else, mark the ending of the previous component
                ongoingComponent = false;
            }

            // Move onto the next node
            listIter = listIter.next;
        }

        return numComponents;
    }
}