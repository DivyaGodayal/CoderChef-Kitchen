## Construct a Binary Tree from Inorder and Postorder Traversal

<p>
<img align="center" alt="Question Screenshot" src="../../Images/Tree-Construction/question.png">
</p>

---

### Solution : 

####  Motivation
We are given inorder and postorder traversal of a Binary Tree and we have to recreate the Binary Tree from the given traversals.

**TIP:** To create a binary tree we need atleast two different traversals. A single traversal can have many different tree structures.

Let us understand how are we gonna approach the problem by taking an example.

<p>
<img align="center" alt="Question Screenshot" src="./../../Images/Tree-Construction/example-tree.png">
</p>

Let us write the `Inorder` and `Postorder` traversal of the above tree.

```
Inorder    = [24,29,38,41,49,51,55,63,77]
Postorder  = [29,24,41,38,51,55,77,63,49]
```
#### Observations derived from the Tree structure and it's traversals :

1. `root` of the tree will always be the last node in it's postorder traversal.
2.  Nodes left to the `root` and Nodes right to the `root` appear in same fashion in it's inorder traversal. From the diagram Node(38) and Node(63) are left and right node of Root(49), they appear in same manner in the `inorder` traversal of the tree. They don`t change their relative order with respect to it's parent.

#### Algorithm
1. Find the last node in the `postorder` traversal.
2. Mark this as root for the current state.
3. Find the index of above node in the `inorder` traversal tree. So everything left to that `index` will be the left subtree and right to the `index` will be the right subtree.
4. Recusrsively repeat the the process from step 1-3 for left and right subtree.



#### Complexity Analysis
* Time Complexity: `O(N^2)` where `N` is the number of nodes. This is beacuse we are searching index of last node in `postorder` traversal in the `inorder` traversal of the tree.
* Space Complexity: `O(N)` where `N` is the number of nodes. The space is occupied by the recursion stack in this case.

#### Link to OJ
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

#### Link to Solution
https://github.com/Arihant1467/CompetitiveProgramming/tree/master/Tree-Construction/solution.py

---
Article contributed by [Arihant Sai](https://github.com/Arihant1467)
