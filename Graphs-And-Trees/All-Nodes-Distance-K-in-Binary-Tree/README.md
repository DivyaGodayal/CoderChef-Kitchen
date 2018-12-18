<p align="center">
<img src="../../Images/k-path.png" width="600">
</p>

---
### Solution 1: Dissolving the Graph solution

#### Motivation

So we are given a tree and we are also given a root node and a target node. We want to get all the nodes which are at a distance of `K` from the target node. If we just forget that this is a tree structure and all we have an unweighted, undirected graph, then finding the solution to this problem simply becomes a level order traversal from the given target node and then returning all the nodes at the `Kth` level.

#### Algorithm

1. This is precisely what we will do in our first solution. We will traverse our given tree and we will construct an adjacency list based structure from it by dissolving the left and right pointers. Once we have our graph, we will do a level order traversal from our target node. 

2. The question that arises here is do we actually need to dissolve the tree into a graph for this to work ? Every node (except the leaves and the root) in a binary tree will have exactly 3 connections.
    * parent
    * left child and
    * right child.
    
3. From a graph's perspective, these three connections are a node's neighbors and become the candidates to be pushed onto the queue during level order traversal. 

4. So, we first make a single pass over the original tree to fix our parent pointers and once we have our parent pointers fixed, we will do a level order traversal from the target node and return a list of all the nodes at the `Kth` level.

#### Complexity Analysis

* Time Complexity: `O(N)` as we make one pass to fix the parent and another pass to do the level order traversal. 
* Space Complexity: `O(N)` for fixing the parent pointers corresponding to each node.

#### Link to OJ

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

---
Article contributed by [Sachin](https://github.com/edorado93) and [Divya](https://github.com/DivyaGodayal)
