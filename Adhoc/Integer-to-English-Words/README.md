<p align="center">
<img src="../../Images/Integer-to-English-Words.png" width="600">
</p>

---
### Solution 1: Recursive Approach

#### Motivation

The basic motivation for this problem is the inherent recursive structure present in the problem. For producing the worded representation of a 6 digit number, we can find 2 english worded representations of the first 3 and last 3 digits respectively and combine the results. This gives rise to a recursive structure that makes the problem easy to solve.

#### Algorithm

1. We will attempt to solve this problem recursively. Before proceeding to solve it recursively, however, let us look closely at the given pattern in the question.
2. Two digit numbers can be solved separately and easily. 
3. For the three digit numbers, we can split them up into 1 + 2 and then recursively solve them individually and then string them up like this `recurse(num[1]) + " Hundred " + recurse(num[2:3])`
4. Similar strategy can be used for bigger buckets like Thousand, Million and finally Billion. We stop at Billion because the max number can be 2^31-1 and that is approximately 2 Billion. So that is where we stop. 
5. Let's try and recursively solve an example for a huge number like 2^31-1 so as to get a better intuition.

<p align="center">
<img src="../../Images/Integer-to-English-Words-IMG1.png" width="600">
</p>

* The example is self explanatory. However, let's look at the recursive steps for all the buckets we can have.
  * If the number > 1e9, then it will have atleast 10 digits. 9 digits have to be solved recursively, and the leftover (in the beginning should be handled as a separte bucket)
  * The next 9 can be split into first 3 and the next 6 and they have to be strung together by "Million". So we have 2 more recursive calls here. 
  * The 6 can be split into two buckets of 3 each and strung together by "Thousand". Again, 2 recursive calls. 
  * We have a bunch of calls for 3 digit numbers. They can be solved by splitting in 1 and 2. The first digit + "Hundred" + the last 2 digits being handled by the only function being used in the code apart from the recursive function. 

`NOTE:` We need to handle a lot of base cases here. Especially the ones which are multiples of 10. And 0 is also a special case here. Don't forget to handle that as well. ;) For further clarifications, look into the code. 

#### Complexity Analysis

* Time Complexity: `O(1)`
* Space Complexity: `O(1)`

#### Link to OJ

https://leetcode.com/problems/integer-to-english-words/description/

---
Article contributed by [Sachin](https://github.com/edorado93)

