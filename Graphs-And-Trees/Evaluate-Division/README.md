![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Evaluate-Division.png)

## SOLUTION

There are certain base cases that can easily be handled right off the shelf either directly or by using some additional data structures.

* If numerator == denominator, return 1.
* If we have already seen the equation (num / den) or (den / num) then we return the answer as is.
* In case we haven't seen either of the alphabets i.e. either the numerator is an alphabet that was not seen in the equations provided or the denominator was the one that was unseen before. In this case we return -1. For this we can simply have a set of alphabets and keep adding the numerator and the denominator to it for every equation seen.

Now that these base cases are out of the picture, we can finally focus on the actual question at hand. Say we are given a bunch of division equations and we are to find `a / e`.

As for `a` in the numerator, we have multiple options in the denominator like `b`, `c`, `d` etc. Say `a / e` can be formed as follows: `(a / c) * (c / m) * (m / p) * (p / e)`. That's the final answer **path**. We, however, do not know that this is the final path. For the program, any of the choices i.e. `b, c or d` might lead to the final solution of `a / e`. This smells like a standard DFS problem because we have to try out all the paths and find the one that leads to a solution.

We consider this as a graph problem G(V, E) where the vertices are the equations, both which are initially given and also the ones we form along the way eg:- `(a / b) * (b / f) = a / f`. Two nodes say X and Y are connected by a **directed edge** X --> Y if *the denominator of X is the same as the numerator of Y*.

Note: we don't actually construct a graph. This is just the representation that is to be followed. We start from the numerator required in the query, say in the example we considered that was `a`. We look at all the children of `a` i.e. all the denominator choices for `a`. In the example we have `b`, `c` or `d`. We recurse on all 3 and in the next recursion, the choice we make becomes the numerator and then we look at its denominators and so on. Have a look at the following graph for better understanding.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Evaluate-Division-Recursion.png)

The path in yellow is what we are looking for. `a -> c -> m -> p -> e` means equations `(a / c) * (c / m) * (m / p) * (p / e)` giving us `a / e` finally. One variable being passed to the DFS is enough to get us the answer. Have a look at the code for the pseudo-code for the search algorithm for this.

```
def dfs(d):
    if d == den:
        return 1

    for child in [denominators of d if any]:
          if child is not visited:
              mark visited
              result = dfs(child)
              if result != -1:
                  return result * value(d / child)

    return -1              
```

**Time Complexity**: The time complexity for any graph based problem is O(V + E). Now, the number of vertices are
all the alphabets we have seen. Let's call that set as A. So V = |A|. As for the edges, we can have edges between every pair of alphabets in the worst case i.e. every alphabet reachable from every other. In this case E = O(V^2). So the time complexity is basically O(V^2).
