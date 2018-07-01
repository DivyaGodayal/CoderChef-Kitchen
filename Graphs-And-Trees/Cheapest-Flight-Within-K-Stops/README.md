## SOLUTION

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Cheapest-Flight.png)

### Dynamic Programming Solution

* There is a very simple dynamic programming based solution to this problem.
* Have a look at the following diagram and then I will explain the recursive relation for the problem.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/DP-cheaptest-flight.png)

* The figure has the DP based recurrence written on it. Essentially, the shortest flight within K stops from `S` to `D`
would have to go through one of the neighbors of `D` or nodes that have an edge to `D` which in the above diagram happen to
be the nodes `U, V and X`.
* That edge, be it `U --> D` or `X --> D` would count towards the total stops because neither `U` nor `X` is the destination. So, then
recurrence relation is

```
dp[k][D] = min(dp[k-1][x] + cost[x --> D]) for all x which have an edge to D.
```

**Time Complexity** = O(n * K)
**Space Complexity** = O(n * K)

### BFS Solution
* This solution is the most natural solution that comes to one's mind when thinking of these kind of problems. You may have come up with Dijkstra's Algorithm and a modification to it, but I tried doing that and didn't work out for me. DP was the way to go initially.
* But, as it turns out, there is a faster alternative to this problem.
* We can use BFS to keep track of the recursion states i.e. the nodes and use them to find the shortest path.
* You might say that BFS cannot be used to find the shortest path in a weighted graph. That is correct, but the constraint here is that of the K stops and hence, the algorithm can only go until a max level of K and not beyond. That is what makes the problem tractable using something like BFS.

**Time Complexity** = O(n^K)
**Space Complexity** = O(n^K)

Essentially, a node gets added once to the queue for initial processing, it gets added again only if BFS discovers an alternate path with smaller cost under K stops to that node. Otherwise not. This is a flight network and it is quite possible that every location is connected to every other location, but we cannot figure out for sure how many times a node would get processed during BFS. It is not possible that all the paths to all the nodes end up improving the shortest path. So, from the look of it i.e. algorithmic complexity wise this algorithm seems worse than DP one but it turns out to be `3X` faster on the leetcode platform.

Have a look at the code for both the solutions to understand the algorithms to their fullest.
