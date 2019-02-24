## Construct a Binary Tree from Inorder and Postorder Traversal

<p>
<img align="center" alt="Question Screenshot" src="../../Images/Binary-Tree-from-Inorder-and-Postorder-Traversal/question.png">
</p>

---

### Solution One : 

####  Motivation
We are given inorder and postorder traversal of a Binary Tree and we have to recreate the Binary Tree from the given traversals.

**TIP:** To create a binary tree we need atleast two different traversals. A single traversal can correspond to many different tree structures.

Let us understand how are we going to approach the problem by taking an example.

<p>
<img align="center" alt="Question Screenshot" src="./../../Images/Binary-Tree-from-Inorder-and-Postorder-Traversal/example-tree.png"  width="600">
</p>

Let us write the `Inorder` and `Postorder` traversal of the above tree.

```
Inorder    = [24,29,38,41,49,51,55,63,77]
Postorder  = [29,24,41,38,51,55,77,63,49]
```
#### Observations derived from the Tree structure and it's traversals :

1. `root` of the tree will always be the last node in it's postorder traversal.
2.  Nodes left to the `root` and Nodes right to the `root` appear in same fashion in it's inorder traversal. From the diagram Node(38) and Node(63) are left and right node of Root(49), they appear in same manner in the `inorder` traversal of the tree. They don't change their relative order with respect to it's parent.

#### Algorithm
1. Find the last node in the `postorder` traversal.
2. Mark this as root for the current state.
3. Find the index of above node in the `inorder` traversal tree. So everything left to that `index` will be the left subtree and right to the `index` will be the right subtree.
4. If we carefully observe the part before `index` in `postorder` traversal and and the part after `index` in `postorder` corresponds to `postorder` traversal of left and right subtree respectively. 
5. Recursively repeat the the process from step 1-3 for left and right subtree.



#### Complexity Analysis
* Time Complexity: `O(N^3)` where `N` is the number of nodes. This is beacuse we are searching index of last node in `postorder` traversal in the `inorder` traversal of the tree for each recursive call and also creating the subarrays during the each recursive call.
* Space Complexity: `O(N)` where `N` is the number of nodes. The space is occupied by the recursion stack in this case.

---

### Solution Two :

####  Motivation
In solution one we were passing subarrays of `postorder` and `inorder` traversals of the tree in each recursive call. Since creating a subarray is also a `O(N)` operation, instead of creating a subarray we will pass indices of `inorder` and `postorder` array which will improve the performance.

#### Algorithm
1. Find the last node in the `postorder` traversal.
2. Mark this as root for the current state.
3. Find the index of above node in the `inorder` traversal tree. So everything left to that `index` will be the left subtree and right to the `index` will be the right subtree.
4. If we carefully observe the part before `index` in `postorder` traversal and and the part after `index` in `postorder` corresponds to `postorder` traversal of left and right subtree respectively. 
5. Recursively repeat the the process from step 1-3 for left and right subtree.

#### Complexity Analysis
* Time Complexity: `O(N^2)` where `N` is the number of nodes. This is beacuse we are searching index of last node in `postorder` traversal in the `inorder` traversal of the tree for each recursive call.
* Space Complexity: `O(N)` where `N` is the number of nodes. The space is occupied by the recursion stack in this case.

---

### Solution Three :

####  Motivation
In all the above solutions we were trying to find the index of the element of the root which is an `O(N)` operation. We can reduce this complexity by keeping a map between `value` and `index` of each element of `inorder` traversal. This will reduce our search opeartion time to `O(1)` time.   

#### Algorithm
1. Find the last node in the `postorder` traversal.
2. Mark this as root for the current state.
3. Find the index of above node in the `inorder` traversal tree. So everything left to that `index` will be the left subtree and right to the `index` will be the right subtree.
4. If we carefully observe the part before `index` in `postorder` traversal and and the part after `index` in `postorder` corresponds to `postorder` traversal of left and right subtree respectively. 
5. Recursively repeat the the process from step 1-3 for left and right subtree.

#### Complexity Analysis
* Time Complexity: `O(N)` where `N` is the number of nodes.
* Space Complexity: `O(N)` where `N` is the number of nodes. The space is occupied by the recursion stack in this case and hashmap of the `inorder` traversal.



#### Link to OJ
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

---
Article contributed by [Arihant Sai](https://github.com/Arihant1467)
