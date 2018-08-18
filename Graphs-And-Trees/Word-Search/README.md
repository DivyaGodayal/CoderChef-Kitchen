![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Word-Search.png)

## Yes, you are right! Its as simple at that.

* Here are the steps:
1. Start from a cell.
2. Go in all directions one by one.
3. For every cell you hit there are 4 ways to take.
4. Take one path at a time and see if you can form the given `word`.
5. If you do, return True.
6. If not then keep repeating the same steps for each cell.


![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Word-Search-1.png)

* In the above diagram, when you reach the cell [1,2] you have 4 directions to take. And the next letter to search for is **R**. Lets take these directions one by one.

A) `Top` - We entered [1,2] from Top. So We won't go there again, since we are not allowed to repeat a cell for a word.
b) `Down` - This cell has the letter 'L' which is not what we are looking for. Hence we return to cell [1,2].
c) `Left` - Left cell has the letter 'B' which is not what we are looking for.
d) `Right` - Right cell is the way to go since it has the letter 'R'.

We follow the same steps as mentioned above from the Right cell and eventually will find the word 'SEARCH'. 

* **Time Complexity** `O(N^2)` for every cell you might go down a path of N cells. 
* **Time Complexity** Recursive stack space depending on the depth of the recursive call.