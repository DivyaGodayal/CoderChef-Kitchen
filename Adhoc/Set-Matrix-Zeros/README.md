<p align="center">
<img src="../../Images/Set-Matrix-Zeros.png" width="600">
</p>


The question seems to be pretty simple but the trick here is that we need to modify the given matrix in place i.e. our `Space Complexity` needs to `O(1)`. There are three approaches to the question as such. The first approach makes use of additional memory while the other two don't.

---
### Solution 1: Additional Memory Approach

#### Motivation

So, the idea here is that we make a pass over our original array and we look for zero entries. 

#### Algorithm

1. We iterate over the given matrix, one element at a time.
2. Say, if we find that an entry (i, j) is 0, then we need to record somewhere the row `i` and column `j`. So, we use two `sets`, one for the rows and one for the columns and :
```
if cell[i][j] == 0 {
    row_set.add(i)
    column_set.add(j)
}
```

3. Finally, we iterate over the original matrix once again and
we see if the row `r` or column `c` had been marked earlier. If any of them was marked, we set this element to 0
```
if r in row_set or c in column_set {
    cell[r][c] = 0
}
```

As we can see here, this method uses an additional space of `O(M + N)` with M and N being the number of rows and columns respectively.

#### Complexity Analysis

* Time Complexity: `O(MN)`
* Space Complexity: `O(M + N)`

---
### Solution 2: O(1) using Sentinal Value

Lets now move onto another solution that does not make use of any additional space, but is not that efficient. 

#### Algorithm

1. The idea here is that we iterate over our original array and if we find an entry, say `cell[i][j]` to be 0, then we iterate over row `i` and row `j` and set all the **non zero** elements to some high negative value (say -1000000). Note, we can't use a value like -1 because the matrix can also have negative values.

2. Finally, we iterate over the original matrix and if we find an entry to be equal to the high negative value (constant defined initially in the code as MODIFIED), then we set it to 0.

The inefficiency here is that we might be considering a row multiple times depending upon if it was modified before or not. We can avoid this by checking while iterating if the row / column has already been modified or not and break if they have.

#### Complexity Analysis

* Time Complexity: `O(MN(M + N))`
* Space Complexity: `O(1)`

---
### Solution 3: Smart In-Place Modification Approach

#### Motivation

This solution is a modification of the original idea that we had. Instead of making use of external memory for keeping track of the row and column that have to be zero'ed, we use the first row and first column of the original matrix itself. 

#### Algorithm

1. We essentially have to mark a row and column to be set to zero but without using any additional memory.
2. So, we have to make use of some entries in the original matrix itself to mark a specific row and column. We use the first entry of the row and the first entry of the column and set them to 0 whenever we encounter a zero entry in a cell belonging to that row and column.
```
if cell[i][j] == 0 {
    cell[i][0] = 0
    cell[0][j] = 0
}
```

3. Since, the first entry of row and column for the first row and first column is the same i.e. `cell[0][0]`, we use an additional variable to tell us if the first column had been marked or not and the `cell[0][0]` would be used to tell the same for the first row.
4. So, we go over our matrix and we mark the first entry of a row and first entry of a column if the condition in the pseudo code above is satisfied.
5. After we have done this, we first use the entries in the first column to set each of the row(s) to zero.
6. Then, we use the first row to zero out the column(s).
7. We then check if `cell[0][0] == 0`, if this is the case, we mark the first row as zero.
8. And finally, we check if the first column was marked, we make all entries in it as zeros.

To see all these loops in action, look at the code.

#### Complexity Analysis

* Time Complexity: `O(MN)`
* Space Complexity: `O(1)`

#### Link to OJ

https://leetcode.com/problems/set-matrix-zeroes/

---
Article contributed by [Sachin](https://github.com/edorado93) and [Divya](https://github.com/DivyaGodayal)
