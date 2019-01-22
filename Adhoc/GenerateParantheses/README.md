## Generate Parantheses

<p>
<img align="center" alt="Question Screenshot" src="./question.png">
</p>


---

### Solution : Backtracking

####  Motivation
So we are given `N` pairs of parentheses and we have to return all the valid expression using these `N` pairs.

Below is the list of all valid expressions for `N = 2`.
#### `( ) ( )`
#### `( ( ) )`

So here's the approach. The length of any expression will always be equal to `N * 2`. So, at every index of the expression we have 2 choices to fill it either `(` or `)`. So  we try to fill every index of the expression recursively either by using `(` or `)` and check the validity of the expression. This can be accomplished with the help of Backtracking. 

Below is the recursion tree formed by backtracking for `N = 2`.

<p>
<img align="center" alt="Recursion tree" src="./complete-recursion-tree.png" >
</p>

As per the recursion tree from the above diagram, if we try forming strings by traversing from root node to every leaf node then we get all possible expression for that `N`. So from the above we have listed all the possible expressions for `N = 2`.

```
 (((( 
 ((()  
 (()(  
 (())  
 ()((  
 ()()  
 ())(  
 ()))  
 )(((  
 )(()  
 )()(  
 )())  
 ))((  
 ))()  
 )))(  
 ))))

```

After a careful observation of the tree and the expressions above, we can see that all these expressions can be formed by making a <b>Postorder Traversal</b> of the tree. Out of these we only add those expressions which are valid. The valid expressions out of these are

```
 ()()
 (())
```
From the above valid expressions we can observe that, the expression where number of open parantheses `(` and close parantheses `)` are equal is the valid one. The paths of the above valid expressions have been highlighted in the below diagram.

<p>
<img align="center" alt="Recursion tree" src="./path-highlighted.png" >
</p>



#### Algorithm
1. We start with an empty string  and mark it as `level = 0` and make a postorder traversal. 
2. During the traversal we will keep track of the opening parantheses `(` and closing parantheses `)` and whenever we encounter such cases where number of closing parantheses are more than opening parantheses we will reject it.
3. At `level = N*2` we check if the count of both open parantheses `(` and closing parantheses `)` is equal to zero. If it is then then its a valid expession.

#### Complexity Analysis
* Time Complexity: `O(2^N-1)` where `N` is the number of pairs of parantheses.
* Space Complexity: `O(N)` where `N` is the number of pairs of parantheses.

#### Link to OJ
https://leetcode.com/problems/generate-parentheses/

---
Article contributed by [Arihant Sai](https://github.com/Arihant1467)
