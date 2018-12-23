<p align="center">
<img src="../../Images/Next-Greater-Element-I/question.png" width="600">
</p>

---
### Solution 1: Brute Approach

#### Motivation

The constraints of the problem are such that you might feel like trying brute approach.

#### Algorithm

1. For each element nums1[i] in `nums1` array, search nums1[i] in `nums2` array.
2. Once you have found the `nums1[i]` in `nums2` array, proceed further in the `nums2` array and find the next bigger element.
3. Once you find the next bigger element, break from the loop and continue to step 1 till you have found next bigger for each element of array `nums1`.
4. If you don't find the next bigger element for any of the element, then return the corresponding next bigger element as -1.

#### Complexity Analysis

* Time Complexity: `O(NM)`, where N is the size of array nums1 and M is the is the size of array nums2.
* Space Complexity: `O(1)`

#### Implementation Notes

We can optimize this approach a little bit by creating a hash table or a dictionary from `nums2` array. The entry of this dictionary for `nums2` would look something like `{Element stored at an index i  : i}`. So now you don't need to search for an element in `nums2`, rather you can just find out its index from the dictionary in constant time and then from this index onwards look up for the next bigger element.

---
### Solution 2: Stacks !

#### Motivation

This approach is not as intuitive as it should be. But is very interesting. Stack is a very good data structure to main history. Where the top would be the latest happening. This is what this approach utilizes. The stack top would always have the latest maximum value.

#### Algorithm

1. Starting the last index iterate the `nums` array, backwards.
2. For every element of `num`'s array compare with the stack top and keeping popping stacks top element until the stack top has a greater element than the current element.
3. If the stack exists then, the next bigger element for the current element is the one at the top of the stack.
4. All the smaller elements which were popped off the stack, have a higher value representative in the for, of a current element.
3. This is because the current value is a higher value. If we look from the left of it. Hence it is added to the stack top.

#### Complexity Analysis

* Time Complexity: `O(M + N)`
* Space Complexity: `O(M * N))`

#### Link to OJ

https://leetcode.com/problems/next-greater-element-i/

---
Article contributed [Divya](https://github.com/DivyaGodayal)
