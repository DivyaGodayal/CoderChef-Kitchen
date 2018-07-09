![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Path-Sum.png)

## SOLUTION

The *brute* way of approaching this problem would be to try all possible paths. Which would essentially mean going down every possible path from every node and checking if the path results in the given sum. 

Lets look at the complexity analysis for this approach:

*Average Case:*

If N is the number of nodes in the tree and the tree is a balanced tree. Every node is visited from the nodes above it which would be height og the tree i.e. logN.

`Average time complexity 
		= No. of nodes in the tree * Number of times each node is visited
		= N * logN
`

[[Diagram]]

*Worst Case:*

If the tree is a skewed tree then every node would be visited from all the nodes above it in the similar fashion as above but since the height of the tree is now N, the complexity is N * N.
`
Worst time complexity 
		= 1 + 2 + 3 + .......+ N-1
		= O(N^2)
`
[[Diagram]]

### Optimal Solution
In the optimal solution we traverse the tree one node at a time in regular depth first fashion. Keeping a track of the sum down any path till that node and calling it the `running_sum`.

[[Diagram]]

Storing these running sum in a dictionary helps to keep a track of what all milestones we have reached so far. Since this is a cummulative sum we can at any time find the difference between any milestone to find the distance for any sub-path.

[[Diagram]]

Here, since we have the target sum i.e. the desired sum for a path we can find out the difference between target_sum and the running_sum for a node and call it the `deviation`. 

		` deviation = running_sum - target_sum`

The deviation tells us how far is our running sum from the target_sum.

[[Diagram to show the negative and positive deviations.]]

Now if we have this present in the dictionary of running_sums then we can say we do have a path in the dictionary which is causing this deviation and could be removed to get a sub-path with desired sum.

[[Diagram to show the subpath and remove of deviation path]]

Since there could be nodes with negative values hence there could be paths with same running_sum. Thus we need to save the count of same running_sums. Since either of these running sums could lead us to a sub-path with desired sum. 

[Diagram to show multiple paths on the same path.]


Time Complexity: Number of nodes in the tree = N.


