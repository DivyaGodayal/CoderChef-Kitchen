![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/LinkedList-Random-Pointer.png)

Before looking at the solution, have a look at how the linked list looks, just to get a better understanding of the question.
![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/LinkedList-RandomPointers.png)

## RECURSIVE SOLUTION

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/LinkedList-RandomPointers-Tree.png)

* The basic idea behind the recursive solution is to consider the linked list like a binary tree. 
* Every node of the Linked List has 2 pointers. So we consider these nodes as belonging to a binary tree. 
* The head of the list becomes the root of the tree.
* So what we basically have to do now is to traverse the binary tree and clone it. The main issue that we need to tackle here is that of loops. So we can have ![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/LinkedList-RandomPointers-Loop.png). We need to handle this in the code. 
* We start from the root node and we keep traversing the tree (list) and we keep generating new nodes whenever we find a node for which the clone has not been generated. For e.g. we were at the node A and we used the next pointer to go to node B and we created B' which is a new node B with the same data. Also, say there was a random pointer from A to B. In this case we don't have to create yet another copy of the node B because B' already exists. We need to take care of this as well. 
* **Time complexity: O(n)** where n is the number of nodes in the list. **Space complexity: O(n)**. If we look closely, we have the recursion stack, then we have the space complexity to keep track of nodes already cloned. But asymptotically, the complexity is O(n)

## ITERATIVE SOLUTION

* The iterative solution to this problem does not model it as a tree and instead simply treats it as a LinkedList. 
* We can solve this in two passes. 
* In the first pass over the original list, we can create an exact clone of the list with consistent **next** pointers. Note that the random pointer are not yet cloned. 
* Additionally, we have a dictionary that maintains old node to new node mapping. We will need it later on. 
* In the second pass we clone the random pointer. The way we do it is like this. The random pointer for A' (A' is the cloned version of the node A) is dictionary value of the node pointed to by the random pointer of A. In case this is unclear, look at the code. 
* **Time complexity: O(n)** because we make 2 passes over the original list. **Space complexity: O(n)** as we have a dictionary containing mapping from old list nodes to new list nodes. Since there are **n** nodes, we have O(n) space complexity.


