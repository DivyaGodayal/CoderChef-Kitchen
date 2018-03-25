 ![alt text](https://raw.githubusercontent.com/edorado93/CoderChef-Kitchen/master/Images/Flatten-Binary-Tree.png)

## SOLUTION

* The solution to this problem uses a recursive approach. 
* Essentially, we perform a preorder traversal on the given tree and recursively flatten the sub-trees and connect them. 
* Let `node` represent the current node for which a recurse call is made. This is the root of the tree that needs to be flattened into a linked list. 
* We recursively flatten the left subtree of this `node` represented by `node->left` and let the result returned by `flattened-left`.
* Then we recursively flatten the right subtree of this `node` and let that result be `flattened-right`. Since this is a linked list, it will have a header and that header node is the one returned by the recursion. So `flattened-right` and 'flattened-left` represent the head nodes of their respective linked lists. 
* All we need to do now is to connect the **tail** of the `flattened-left` linked list with the head of `flattened-right` linked list. So we iterate over the `flattened-left` linked list and we reach the last node and we connect it to the `flattened-right` linked list thus giving us a combined flattened linked list for the given `node`. 
* **Time Complexity** is O(n) because we are simply doing a pre-order traversal and considering all the nodes exactly once. Also, the sspace complexity is O(n) for the recursion stack.
