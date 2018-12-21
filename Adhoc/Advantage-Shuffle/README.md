<p align="center">
<img src="../../Images/AdvantageShuffle/question.png" width="600">
</p>

---
### Solution 1: Be Greedy !!

#### Motivation

We need to form pairs of elements in A and elements in B, such that `A[i] > B[i]`, i is the index of the array. Comparing with all the permutations of A would be `N!` and hence definitely not recommended.

Consider two arrays:
```
A = [1, 2, 3, 4]
B = [1, 2, 3, 4]
```

`Possible Pairing - Advantage - 2`

 A | B
---|---
`4`|`1`
`3`|`2`
 1 | 3
 2 | 4

In the above example, if we pair up A's `4` and B's `1`, we have lost the chance of pairing up B's `1` with a better candidate, which might be smaller number than `4` and hence 4 could be utilized some where else.

`Better Pairing - Advantage - 3`

 A | B
---|---
`2`|`1`
`3`|`2`
`4`|`3`
1  |4

As seen in the above example if we paired the lowest A's with lowest B's initially, we would have more pairs. The basic intuition for this problem is to be greedy.

Here by greedy we mean start with the smallest values in A and start pairing with the smallest values from B. This would ensure that a lower value in A is matched to a lower value in B. If not then we look for other higher values. Directly jumping on to higher values in A might lead to wrong pairs at the start as described above and the smaller values in `A` might not find any suitable partner. :)

>Starting with smaller values of A makes sure the smaller values in A are utilized first leaving us with bigger values for later bigger values of B. Giving us more chances of forming advantage pairs.

#### Algorithm

1. Sort `A` in increasing order of value.
2. Reform the list `B` to also store the original indices of each element. This index is to be used later on, to place the `shuffled array A` element corresponding to the correct `B`'s element.
3. Now sort the array `B` on the basis of value, in increasing order.

<p align="center">
<img src="../../Images/AdvantageShuffle/Algorithm1.png" width="600">
</p>

4. Take a new array `shuffled_A` to be returned.
5. Iterate both the sorted arrays using index pointers say, i and j.
6. If at any point element in `A` is greater than element in `B` then this pair is useful in increasing the advantage. Place it in the shuffled array at the correct spot using the corresponding index value from array `B`.
7. Else, The element in `A` is added to a list of remaining elements, to be used later.

<p align="center">
<img src="../../Images/AdvantageShuffle/Algorithm2.png" width="600">
</p>

8. After we are done with finding all the advantage elements in `A` and placing them in the correct spot in `shuffled_A`. We can put all the remaining non advantage elements of A in the empty spots of `shuffled_A`. Since, the elements in these empty spots do not count towards the advantage, hence their placement doesn't matter.

<p align="center">
<img src="../../Images/AdvantageShuffle/Algorithm3.png" width="600">
</p>

#### Complexity Analysis

* Time Complexity: `O(NlogN)` since we have to sort the elements to get a list A and B.
* Space Complexity: `O(N)`, where N is the size of array A. All the elements of A might not classify for an advantage over B's element and remaining list size could get as big as size of array A.

#### Link to OJ

https://leetcode.com/problems/advantage-shuffle/

---
Article contributed by [Divya](https://github.com/DivyaGodayal).
