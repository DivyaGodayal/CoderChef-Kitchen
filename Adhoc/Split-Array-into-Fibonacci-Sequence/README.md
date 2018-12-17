<p align="center">
<img src="../../Images/Fibonacci-Sequence.png" width="600">
</p>

The question asks us to split the original string into a sequence of numbers that form a fibonacci sequence with certain conditions being satisfied.

---
### Solution 1: Greedy

#### Motivation

The major condition that really helps reduce the solution complexity is that any number in the fibonacci sequence that we consider should not be greater than 2^31 - 1. That means we only have to consider substrings of length <= 11 for elements of our potential fibonacci sequence. Now, from the looks of it, this might seem like a classical dynamic programming based question because essentially we need to see at what all points we can cut the original sequence eg:

```
2435443212

* 2 | 435 | 4432 | 12
* 243 | 54 | 4321 | 2
* 24 | 35 | 44 | 32 | 12
```

As we can see, we have so many options. Essentially, every point becomes a potential cutting point in the original sequence. Looking like this, we have 2^n possible choices because at every index, we can either split or not. So we would have 2^200 possible choices which is a lot. Hence, DP.

But wait a minute, what if I tell you there's a better solution ? :P

<p align="center">
<img src="https://vignette.wikia.nocookie.net/adventuretimewithfinnandjake/images/6/66/Really_a_pony_version_of_a_meme_some_bronies_really_2fb4eedd3de7d2f02ac5b5b683891f6d.jpg/revision/latest?cb=20121113202035" width="400">
</p>

#### Algorithm

1. There's a nice property of this problem that we can exploit and get a much more efficient solution. If you look closely at any fibonacci sequence, you will see that any fibonacci sequence is essentially defined by the `first two` numbers only. Rest of the numbers can be generated iteratively.

2. So, all we have to do is that we need to consider all possibilities for just the first two numbers and that would give us all possible fibonacci sequences. 

3. For the third number onwards, of a given fibonacci sequence under processing, we can do simple string matching with the original string and move on to the fourth number and so on. 

Let's have a look at the pseudocode for the algorithm

```
for i in 0..10
  for j in i + (0..10)
    first_number = sequence[0 : i + 1]
    second_number = sequence[i + 1 : j]

    if first_number < 2^31 - 1 and second_number < 2^31 {
        result, fib_seq = checkFib(first_number, second_number, sequence)
        if result == True {
            return fib_seq
        }
    }
```

#### Complexity Analysis

* Time Complexity: O(11 \* 11 \* n) = `O(n)`
* Space Complexity: `O(1)`

#### Link to OJ

https://leetcode.com/problems/split-array-into-fibonacci-sequence/

---
Article contributed by [Sachin](https://github.com/edorado93) and [Divya](https://github.com/DivyaGodayal)

