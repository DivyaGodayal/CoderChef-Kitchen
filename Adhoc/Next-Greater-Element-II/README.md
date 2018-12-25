<p align="center">
<img src="../../Images/Next-Greater-Element-II/question.png" width="600">
</p>

This problem is very similar to [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/).

<p align="center">
<img src="../../Images/Next-Greater-Element-II/algorithm_1.png" width="500">
</p>

A circular array is the equivalent of the original array elements repeated twice. Hence we can imitate the circular nature of the array by making two passes through the array.

<p align="center">
<img src="../../Images/Next-Greater-Element-II/algorithm_2.png" width="500">
</p>

---
### Solution 1: Brute Approach

#### Motivation

The Brute approach is the most intuitive approach given the problem statement. However, it gives a time limit exceeded on the OJ.

#### Algorithm

1. Since this question has circular array, so we can double up the original array to form an array `doubledNums`. Since we repeat all the elements, the ending elements would be followed by the starting elements.
2. Each element, let's say `n`, in `nums` array would have the same index `i` in `doubledNums`.
3. For the element at index `i` in the `nums` array, we search for the next largest element starting from index `i+1` in the `doubledNums` array.
4. Once you find the next bigger element, break from the loop and continue to step 2 till you have found next bigger for each element of array `nums`.
5. If you don't find the next bigger element for any of the elements, then return the corresponding next bigger element as -1.

#### Complexity Analysis

* Time Complexity: `O(N^2)`, where N is the size of array `nums`.
* Space Complexity: `O(N)`, to double up the array.

---
### Solution 2: Stacks !


#### Algorithm

The steps are same as described for [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/).
The only differences are:

1. The given array for this problem is a circular array. Hence, in the algorithm we deliberately go through the array twice. Since, going through the array twice is similar to imitating a circular array, we eventually get the next greater element for all the elements if not on the first pass.

2. This problem has only one array, we need to return a list of next greater for all elements of the same array in which we are looking for next greater element, unlike the [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) problem. So we do not need an extra dictionary to compile results for another array.

#### Implementation Notes

A little optimized and may be a better way of doing this  would be to first find the largest element in the array and using that as the starting point instead of `2N` and then moving backwards. Choosing the greatest element as the starting point helps since this element won't need any second pass in the array for correcting its next greater. Also, all the elements ahead of it won't have to go beyond the greatest element in the array. So it makes sense to use that as the starting point.

#### Complexity Analysis

* Time Complexity: `O(N)`, where N is the size of array nums.
* Space Complexity: `O(N)` for the stack.

#### Link to OJ

https://leetcode.com/problems/next-greater-element-ii

---
Article contributed [Divya](https://github.com/DivyaGodayal)
