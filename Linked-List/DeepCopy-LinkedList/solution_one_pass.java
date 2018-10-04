public class Solution {
  // Visited dictionary to hold old node reference as "key" and new node reference as the "value"
  HashMap<RandomListNode, RandomListNode> visited = new HashMap<RandomListNode, RandomListNode>();

  public RandomListNode getClonedNode(RandomListNode node) {
    // If the node exists then
    if (node != null) {
      // Check if the node is in the visited dictionary
      if (this.visited.containsKey(node)) {
        // If its in the visited dictionary then return the new node reference from the dictionary
        return this.visited.get(node);
      } else {
        // Otherwise create a new node, add to the dictionary and return it
        this.visited.put(node, new RandomListNode(node.label));
        return this.visited.get(node);
      }
    }
    return null;
  }

  public RandomListNode copyRandomList(RandomListNode head) {

    if (head == null) {
      return null;
    }

    RandomListNode oldNode = head;

    // Creating the new head node.
    RandomListNode newNode = new RandomListNode(oldNode.label);
    this.visited.put(oldNode, newNode);

    // Iterate on the linked list until all nodes are cloned.
    while (oldNode != null) {
      // Get the clones of the nodes referenced by random and next pointers.
      newNode.random = this.getClonedNode(oldNode.random);
      newNode.next = this.getClonedNode(oldNode.next);

      // Move one step ahead in the linked list.
      oldNode = oldNode.next;
      newNode = newNode.next;
    }
    return this.visited.get(head);
  }
}