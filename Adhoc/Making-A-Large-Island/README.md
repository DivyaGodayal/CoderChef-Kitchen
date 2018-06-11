## SOLUTION

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Making-A-Large-Island.png)

* So, the question essentially asks us to find the size of the largest island given and we are allowed to
flip at most one of the zeros given in the matrix.
* An island is defined by a portion of the matrix all of which contain 1s. Note that we cannot connect two
cells if they are diagonally connected. We can only connect cells that are adjacent in 4 directions
  * (i + 1, j)
  * (i - 1, j)
  * (i,  j + 1)
  * (i, j - 1)

* Before solving this problem, let us look at how we would ideally solve a slightly simpler problem of finding
the largest island in a given matrix. No flips allowed. This is much easier to solve.
* Normally, such problems are easily solvable if we model our problem as a graph.
* So, we model the problem as a graph G(V, E) where each cell represents a vertex and an edge u --> v would exist
in our graph is the cells u and v are adjacent to each other either horizontally or vertically.
* This would be an undirected, unweighted graph. All that is left to do now is to find the size of the largest
connected component in this graph.
* Consider the pseudo-code below.

```
function dfs_util()
{
   ans = 0
   for v in vertices
   {
      if v not already visited
      {
          size_of_connected_component = dfs(v)
          ans = max (ans, size_of_connected_component)
      }
   }

   return ans
}
```

* Note, in the above function, the call to `dfs` is just the normal depth first search traversal that we perform on a given graph and the pseudo-code for the same is left out in this article.
* Now, this was pretty easy. Wasn't it ? Let's move onto the actual problem at hand. We will solve this problem where we are allowed switches as well as en extension of this simple graph problem.
* Have a look at the pseudo-code

```
function dfs_util()
{
   component_to_size = dictionary
   vertex_to_component = dictionary
   visited = dictionary

   connected_component_number = 0
   for v in vertices
   {
      if v not already visited
      {
          size_of_connected_component = dfs(v)
          component_to_size[connected_component_number] = size_of_connected_component
          vertex_to_component[v] = connected_component_number
          connected_component_number += 1
      }
      else
      {
          vertex_to_component[v] = visited[v]
      }
   }

   return ans
}
```

* Let's see what is happening here
* Normally, we store a boolean value in the `visited` dictionary so that we avoid going in loops in our graph traversal. Here, we would store the component number in which this vertex was discovered. So, instead of simply boolean values, we would have integer values representing the component number for that vertex. The visited dictionary is updated in the `dfs` function.
* Additionally, we use a dictionary called `component_to_size` that stores the number of vertices that are a part of that component number.
* Once we have these dictionaries filled up, let's see where we would be using them. Have a look at the diagram below:


![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Large-Island-Logic.png)

* Now, the main idea is that we we iterate over our matrix and consider all of the '0's for flipping. One at a time.
* When we are considering a 0 at a certain cell `(i, j)`. we want to see if flipping this cell would lead to combining some other components or not. If we can combine components because of this, we do that and see the size of new islands we can form this way.
* In this way, we can see the effect of flipping a single 0 in O(1) time and all the time complexity went into the connected components algorithm we discussed before which is pretty standard.
* **Time Complexity** O(V + E) = O(M * N) where the matrix has M rows and N columns.
* **Space Complexity** O(M * N) because we are storing the connected component number for every element in the matrix. 
