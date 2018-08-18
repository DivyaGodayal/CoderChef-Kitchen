![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/bus_routes.png)

# Solution

* The question seems simple at first. It is in fact a really simple question if you can pick up on a small caveat involved here and come up with the right algorithm.

* Usually, these type of questions are best solved when you convert the problem into a **graph** based problem and usually, either Breadth first search or the depth first search algorithm is the right way to go about solving these kind of problems.

* One naîve strategy to solving this question would be to consider every bus stop as a node and connect all of these nodes together according to the question's description.
  - What we can do here is that we connect all of the bus stops on a single route (and they will form a cycle because the bus on this route can reach any of these stops and it loops forever between them.).
  - Also, we will have to assign weights to edges here. So all the edges between vertices (bus stops) on a single rout will have `0` edge weights because a person doesn't have to change the bus to travel between these stops as they lie on the same bus route.
  - For all the other edges we will have an edge weight of `1`.

* Once we have all these edges in place, we can apply find the shortest path in this undirected, weighted graph from ***a*** starting point and the destination point.

* We say a given starting point because the starting point can be a part of multiple bus routes. Which bus you pick up for the starting bus route determines the starting point for the person and eventually the shortest path to the destination.

* Since we can have multiple starting points here, we will have to try out all of them. There is not other alternative for this. We have to start at each of the bus routes that contain our source or the starting bus stop and find the shortest path to the destination or the final bus stop and see which route gives the smallest shortest distance value.

* This algorithm is not incorrect per say. But, it is highly inefficient. Consider the following scenario.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/bus_routes_diag1.png)

* Here, we have two bus routes. The first one has 3 bus stops in it and the other one has 4 bus stops in it. Now, say the person starts at the bus stop `7` and he wants to go to the bus stop `10`.

* From the diagram it is clear enough that the bus stop `10` is not on the bus route that the bus stop `2` is on. ***So, there is no point in processing vertices (bus stops) 2 and 1 and we can directly jump to the second bus route that has 10,2,3 and 9. We can do that because the bus stop 2 is a part of both the bus routes.***. And here again, we can simply see that the bus stop `10` is a part of this bus route. We don't need to go through any shortest path algorithm for this. This information can be stored in a hash table and can be accessed in constant time.

## Optimal Solution

* This idea we just discussed is what fuels the optimal solution.

* Instead of treating each bus stop as a node in our graph, we treat each bus route as a node in our graph. There is an **undirected edge** between two nodes in our graph if the corresponding bus routes share one or more bus stops.

* Note that now we don't have to assign any edge weights here. Every edge has a weight of 1 and so we can leave out these edge weights.

* The question now becomes finding the shortest path from a source to a destination in an undirected, unweighted graph and ***breadth first search*** is the best algorithm for this.

* Have a look at a sample graph from the bus routes to get a better idea of how the algorithm would process them.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/bus_routes_diag2.png)

* Here is the pseudo-code for this algorithm.

```
1. Create a dictionary mapping bus stops to what all bus routes they are a part of.
2. Create virtual nodes for each bus route and build adjacency list connecting bus routes if they share a common bus stop.
3. Apply BFS from all possible starting spots i.e. all the nodes or bus routes that have the starting bus stop as one of their constituent bus stops.
4. Find shortest path to the destination bus route. The only difference from a standard BFS is that we have multiple starting nodes. But that hardly effects the overall complexity.
```

* **Time Complexity**: `O(V + E)` where V = number of bus routes, E = number of edges which in the worst case would be `O(V<sup>2</sup>)`. Also, creating the adjacency list takes time = `O(V<sup>2</sup>)` considering set intersection is `O(1)`.

* **Space Complexity**: `O(V)` where V = number of bus routes.
