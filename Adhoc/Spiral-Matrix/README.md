![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Spiral-Matrix.png)

## SOLUTION

 The question asks us to print the matrix in a spiral format. So this is how we would go about printing the matrix if there are N rows a
    nd M columns
 * 1st row
 * Mth column
 * Nth row
 * 1st column
 ---
 * 2nd row
 * (M - 1)th column
 * (N - 1)th row
 * 2nd column

 ... and so on. This looks like it can be solved recursively on the face of it. Beacuse once we are done printing the outermost structur
    e or the perimiter to say of the given matrix, all that is left is the inner portion which is a matrix in iteself and the same process
    can be repeated for it. So we will employ a recursion based solution to this problem.

The parameters to the given recursive function are the following 4
* Starting row (s_r)
* Starting column (s_c)
* Ending row (e_r)
* Ending column (e_c)

We start our indices `i` and `j` at `s_r and s_c` and the first step is to print out the first row. While printing out the first row, note that we only have to increment the column value i.e. `j` and not the row `i`.

Once the first row has been printed, we move on to printing out the last column. So `j = e_c - 1` (Considering 0 based indexing) and `i` is something that has to be updated. Note: The first element of the last column has already been printed as a part of the printing out of the first row. So we shouldn't print it again.

In a similar fashion we now print out the last column starting from `i=1 and j=e_c - 1`. We keep updating the row index until we reach the last row and at that point we have completely printed out the last column. Now we shift to printing the last row from last column to the first column i.e. in reverse thus adhering to the spiral nature of the printing required by the question. Note: We have already printed out the last element of the last row as a part of printing out the last column. So we shouldn't print it again.

We keep printing in this fashion, first the last row and then the first column from bottom to top. When we reach the first element i.e. `i = s_r and j = s_c` that means we have printed out the perimeter and now we can recurse on the reamining matrix i.e. `(s_r + 1, s_c + 1, e_r - 1, e_c - 1)`.

Have a look at the code for some edge cases and better clarity.


