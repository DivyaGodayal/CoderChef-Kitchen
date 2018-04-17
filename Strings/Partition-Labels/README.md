![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Partition-Labels.png)

## SOLUTION

* The question asks us to partition the given string in such a way so that each character only occurs in just a single partition. 
* We also need to find the maximum number of partitions. eg:- For a string `abcde` we can have a partition like `abc`,`de`and hence the answer would be `[3,2]` but as you can see, the optimal answer here is `[1,1,1,1,1]` because of partitions `a`,`b`,`c`,`d`,`e`.
* The core algorithmic technique used behind this question is INTERVAL SCHEDULING. 
* **First step** is to find out intervals for all the individual characters. We will have 26 intervals in all since we have 26 unique characters in the worst case in the string.
* Once we have the intervals, they will look something like this for the given example in the question `[('a', [0, 8]), ('c', [4, 7]), ('b', [1, 5]), ('e', [10, 15]), ('d', [9, 14]), ('g', [13, 13]), ('f', [11, 11]), ('i', [17, 22]), ('h', [16, 19]), ('k', [20, 20]), ('j', [18, 23]), ('l', [21, 21])]`
* Now we need to sort these intervals according to the starting indices. 
* Then, we start from the very first interval. Note: It doesn't matter what character occurs first. We are just concerned with the first interval in the sorted order to start off. For our example that interval is that of 'a' = [0,8]
* We keep iterating over the sorted list of intervals. 
  * If We get an overlapping interval with the current one, we merge the two intervals and thus effectively, increase the current partition's length.
  * If we get an interval that is not overlapping, then we end the current interval and hence record the partition's size and start the next interval / partition. And so on. 

  eg:- We have the first interval as [0,8]. The next interval in the sorted order is [1,5]. This is overlapping and the new interval is [0,8]. The next interval is [4,7] and this again is overlapping. Updated partition is [0,8]. The next interval is [9,14] and this is clearly not overlapping with [0,8]. So we end the current partition and record its size as 8-0+1 = 9 and start the next partition from [9,14] as the initial boundaries. 
* **Time Complexity**: O(n). Note, we sort the character intervals which are 26 at max. 
* **Sace Complexity**: O(1) as we need a dictionary of 26 elements and then an array of 26 intervals for sorting and processing. 26 is fixed for the given problem as the number of characters. 
