
## SOLUTION

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Sum-of-Distances-Tree.png)

Let's look at what the question is asking us to do here. Consider the following tree.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Diag-1-Sum-of-Distances.png)

In the example above, the sum of paths for the node A i.e. the number of nodes on each path from A to every other vertex in the tree is 9. The individual paths are mentioned in the diagram itself with their respective lengths. 
Similarly, consider the sum of distances for the node C. 

```
C --> A --> B (Length 2)
C --> A (Length 1)
C --> D (Length 1)
C --> E (Length 1)
C --> D --> F (Length 2)
Sum of distances (C) = 2 + 1 + 1 + 1 + 2 = 7
```

This is known as the sum of distances as defined for just a single node A or C. We need to calculate these distances for each of the nodes in the tree. 

Before actually solving this generic problem, let us consider a simplified version of the same problem which says we just need to calculate the sum of distances for a given node, but we will only consider the tree rooted at the given node for calculations. 
So, for the node C, this simplified version of the problem would ask us to calculate:

```C --> D (Length 1)
C --> E (Length 1)
C --> D --> F (Length 2)
Simplified Sum of Distances (C) = 1 + 1 + 2 = 4
```
This is a much more simpler problem to tackle recursively and would prove to be useful in solving the original problem.
Consider the following simple tree.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Diag-2-SOD.png)

The nodes B and C are the children of the root i.e. A. 

**We are trying to see what information can we use from subproblems i.e. children, to compute the answer for the root A .**

Note, here we simply want to calculate the sum of paths for a given node X, given that all of the paths are to its successors. 
There are no downwards going paths from the node B and hence, sum of paths is 0 for the node B in this tree. Let's look at the node C . So this node has 3 different successors in F, D and E . The sum of distances are as follows:

```C --> D (Path containing just 1 edge, hence sum of distances = 1)
C --> D --> F (Path containing 2 edges, hence sum of distances = 2)
C --> E (Path containing just 1 edge, hence sum of distances = 1)
```

Clearly the sum of all the paths from the node C to all of it's decedents is 4 and number of such paths going down are 3. 
Note the difference here. The sum_of_distances here counts the number of edges in each path instead of counting each path as 1 like number_of_paths .

If you look closely, you will realize that the number of paths going down is always going to be number of nodes in the tree we are considering (except the root). So, for the tree rooted at C, we have 3 paths,  one for the node D, one for E and one for F. So, the number of paths from a given node to the successor nodes is simply the total number of descendent nodes reason being that this is a tree. So, no cycles or multiple edges.

Now, consider the node A. Let us look at all the new paths that are being introduced because of this node A. Forget the node B for now and just focus on the child node C corresponding to A. The new set of paths that we have are:

```A --> C (Path containing just 1 edge, hence sum of distances = 1)
A --> (C --> D)    (Path containing 2 edges, hence sum of distances = 2)
A --> (C --> E)    (Path containing 2 edges, hence sum of distances = 2)
A --> (C --> D --> F) (Path containing 3 edges, hence sum of distances = 3)
```

Except for the first path A → C, all the others are the same as the ones for the node C except that we have simply changed all of them and incorporated one extra node A.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Diag-3-SOD.png)

If you look at the diagram above you will see a tuple of values next to each of the nodes A, B and C. 
```
(X, Y) where
X is the number of paths originating at that node and going down to the decedents.
Y is the sum of distances for the tree rooted at the given node.
```

Since the node B doesn't have any further children, the only path it is contributing is the path A --> B to A's tuple of (5, 9) above. So let's talk about C. 

C had 3 paths going to its successors. Those three paths (extended by one more node for A) also become 3 paths from A to it's successors, among others. 

```
N-Paths[A] = (N-Paths[C] + 1) + (N-Paths[B] + 1)
```

That is the exact relation we are looking for as far as the number of paths (= number of successor nodes in the tree) are concerned. The 1 is because of the new path from the root to it's child i.e. A --> C in our case. 

```
N-Paths[A] = 3 + 1 + 0 + 1 = 5
```
As far as the sum of distances is concerned, take a look at the diagram and the equations we just wrote and the following formula becomes very clear

```Sum-Dist[A] = (N-Paths[C] + 1 + Sum-Dist[C]) + (N-Paths[B] + 1 + Sum-Dist[B])
Sum-Dist[A] = (3 + 1 + 4 + 0 + 1 + 0) = 9
```

The main thing here is N-Paths[C] + Sum-Dist[C] . We sum these up because all of the paths from C to its descendants ultimately become the paths from A to its descendants except that they originate at A and go through C and so each of the path lengths are increased by 1. There are N-Paths[C] paths in all originating from C and their total length is given by Sum-Dist[C] .

Hence the tuple corresponding to A = (5, 9). The Python code for the algorithm we discussed above is as follows.

https://gist.github.com/edorado93/f89850fc7353c7662fac133ebd49c793.js

### The Curious Case of the Visited Dictionary :/

If you look at the code above closely, you'll see this 

```
# Prevents the recursion from going into a cycle.        
self.visited[vertex] = 1
```

The comment says that this visited dictionary is for preventing the recursion from entering a cycle.

If you've paid attention till now, you know that we are dealing with a tree here. 

The definition of a tree data structure doesn't allow cycles to exist. If a cycle exists in the structure, then it is no longer a tree, it becomes a graph. In a tree, there is exactly one path between any two pair of vertices. A cycle would mean there are more than one paths between a pair of vertices. Look at the figures below.


![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Diag-4-SOD.png)

The structure on the left is a tree. It has no cycles in it. There is a unique path between any two vertices.

The structure on the right is a graph, there exists a cycle in the graph and hence there are multiple paths between any pair of vertices (for this graph it so happens that any pair of vertices have more than one path. Not necessary for every graph). 

Almost always, we are given the root node of the tree and we can use the root node to traverse the entire tree without having to worry about any cycles as such. However, if you've read the problem statement clearly, it does not state anything about root of the tree. 

That means that there is no designated root for the tree that given in the question. This could mean that a given tree can be visualized and processed in so many different ways depending upon what we consider as the root. Have a look at multiple structures for the same tree but with different root nodes.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Diag-5-SOD.png)

So many different interpretations and parent child relationships possible for . a given unrooted tree. 

So, we start with the node 0 and do a DFS traversal of the given structure and in the process we fix the parent child relationships. Given the edges in the problem, we construct an undirected graph like structure which we convert to the tree structure. Taking a look at the code should clear out some of your doubts.

https://gist.github.com/edorado93/ecbea2efcb9a3c87249e4444f35e68fb.js

Every node would have one parent. The root won't have any parent and the way this logic is, the node 0 would become the root of our tree. Note that we are not doing this process separately and then calculating the sum of distances downwards. Given a tree, we were trying to find, for every node, the simplified sum of distances for the tree rooted at that node. 

So, the conversion from the graph to the tree happens in one single iteration along with finding out the sum of distances downwards for each and every node.

https://gist.github.com/edorado93/f89850fc7353c7662fac133ebd49c793.js

Posted the code again so that the visited dictionary makes much more sense now. So, one single recursion doing all that for us. Nice!

### Bringing it all together

Now that we have our tree structure defined and also the values of sum of distances going downward defined for us, we can use all of this information to solve the original problem of Sum of Distances in a Tree. 

How do we do that ? It's best to explain this algorithm with the help of an example. So we will consider the tree below and we will dry run the algorithm for a single node. Let's have a look at the tree we would be considering.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Diag-6-SOD.png)

The node for which we want to find the sum of distances, is 4. Now, if you remember the simpler problem we were trying to solve earlier, you know that we already have two values associated with each of the nodes

1. `distances_down` Which is the sum of distances for this node **while only considering the tree beneath**.
2. `number_of_paths_down` which is the number of paths / nodes in the tree rooted at the node under consideration. 

Let's look at the annotated version of the above tree. The tree is annotated with tuples (distances_down, number_of_paths_down) .

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Diag-7-SOD.png)

Let's call the value we want to compute for each node as sod which means sum of distances. 

Let us assume that we have already computed the answer for the parent node of 4 in the diagram above. So, we now have the following information for the node labelled 2 available 

```
(sod, distances_down, number_of_paths_down) = (17, 4, 3)
```

Let's rotate the given tree and visualize it in a way where 2 is the root of the tree essentially.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Diag-8-SOD.png)

Now, we want to remove the contribution of the tree rooted at 4 from sod(2). Let us consider all of the paths from the parent node 2 to all other nodes except the ones in the tree rooted at 4 . 

```2 --> 5 (1 edge)
2 --> 1 (1 edge)
2 --> 1 -->7 (2 edges)
2 --> 1 --> 7 --> 9 (3 edges)
2 --> 1 --> 7 --> 10 (3 edges)
Number of nodes considered = 6
Sum of paths remaining i.e. sod(2) rem = 1 + 1 + 2 + 3 + 3 = 10
```

Let's see how we can use the values we already have calculated to get these updated values. 

```* N = 8 (Total number of nodes in the tree. This will remain the same for every node. )
* sod(2) = 17
* distances_down[4] = 1
* number_of_paths_down[4] = 1
* (distances_down[4] does not include the node 4 itself)
N - 1 - distances_down[4] = 8 - 1 - 1 = 6
* sod(2) - 1 - distances_down[4] - number_of_paths_down[4] = 13 - 1 - 1 - 1 = 10
```

If you remember this from the function we defined earlier, you will notice the contribution of a child node to the two values distances_down and number_of_paths_down is `n_paths + 1` and `n_paths + s_paths + 1` respectively. Naturally, that is what we subtract to obtain the remaining tree.

https://gist.github.com/edorado93/b7076f6f2cda42a672c8c8e75531e0d0.js

`sod(4)` represents the sum of edges on all the paths originating at the node 4 in the tree above. Let's see how we can find this out using the information we have calculated till now. 

`distances_down[4]` represents the answer for the tree rooted at the node 4 . So, that will directly add to the final answer. Let's call this value own_answer . Now, let's account for all the other paths. 

```4 --> 2 (1 edge)
4 --> 2 --> 5 (1 + 1 edge)
4 --> 2 --> 1 (1 + 1 edge)
4 --> 2 --> 1 -->7 (1 + 2 edges)
4 --> 2 --> 1 --> 7 --> 9 (1 + 3 edges)
4 --> 2 --> 1 --> 7 --> 10 (1 + 3 edges)
own_answer = 1
sod(4) = 1 + 1 + 2 + 2 + 3 + 4 + 4 = 17
sod(4) = own_answer + (N - 1 - distances_down[4]) + (sod(2) - 1 - distances_down[4] - number_of_paths_down[4]) = 1 + 6 + 10 = 17
```

Let's look at the code and bring all of the things we discussed in the example above, together.

https://gist.github.com/edorado93/99d8fcffc5fbdd7957e488096ddfd59b.js

The recursive relation for this portion is as follows:

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Diag-9-SOD.png)
