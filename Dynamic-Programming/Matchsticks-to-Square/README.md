![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/matchsticks-to-square.png)

* Let us first look at an example to understand the various possibilities for the matchsticks and what all arrangements are possible.

* e.g.: `[1,1,1,1,2,2,2,2,3,3,3,3]` In this case a square of side `6` can be formed and we have 4 each of `1`, `2` and `3` and so we can have each square side formed by `3 + 2 + 1 = 6`.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/matchsticks-diag-1.png)

* We can clearly see in the diagram above that the 3 matchsticks of sizes `1`, `2` and `3` combine to give one side of our resulting square.

* If we look at this problem from an algorithmic perspective, then essentially we have to split the given array into 4 subsets where all of these subsets are:
  - mutually exclusive i.e. no specific element of the array is shared by any two of these subsets, and
  - have the same sum which is equal to the side of our square.

* Now, we know that we will have 4 different subsets. The sum of elements of these subsets would be `sum(arr) / 4` where `sum(arr)` represents the sum of all the values in the array. **Note:** if the sum if not divisible by 4, that implies that no such 4 subsets of equal value are possible and we don't need to do any further processing on this.

* The only question that remains now for us to solve is,
` what subset a particular element belongs to? `. If we are able to figure that out, then there's nothing else left to do. But, since we can't say deterministically which of the 4 subsets would contain a particular option, we **TRY OUT ALL THE OPTIONS**.

## Recursive Solution

* It is possible that a matchstick ***can*** be a part of any side of the resulting square, but which one of these choices leads to the formation of an actual square is something we don't know. So, we try out everything.

* This means that for every matchstick in our given list / array, we essentially have 4 different options (each representing the side of the square or subset that this element can be a part of). We try out all of them and keep on doing this in a recursive fashion until we exhaust all of the possibilities or until we find an arrangement of our matchsticks such that they form the 4 sides of a square.

  ```
  if (no matchstick remaining) and (4 sides formed), then {
    return True
  }

  for i in 1..4, do {
    if matchstick[index] + sides[i] <= target, then {
      sides[i] += matchstick[index]
      recurse()
      sides[i] -= matchstick[index]
    }
  }
  ```

* **Time Complexity** : `O(4<sup>n</sup>)` because we have a total of `n` sticks and for each one of those matchsticks, we have 4 different possibilities for the subsets they might belong to or the side of the square they might be a part of.

* **Space Complexity** : For recursive solutions, the space complexity is the stack space occupied by all the recursive calls. The deepest recursive call here would be of size O(n) and hence the space complexity is `O(n)`

### Implementation Details

* This solution is very slow as is. However, we can speed it up considerably by a small trick and that is to sort our matchsticks sizes in reverse order and consider the matchsticks in this reverse sorted order.

* The reason for this is that if the set of matchsticks would be invalid, we would find that our very quickly because of the invalidity being caused by a large matchstick. e.g. `4,4,4,8`. In this case we can have a square of size 5 but the largest side 8 doesn't fit in anywhere i.e. cannot be a part of any of the sides (because we can't break matchsticks according to the question) and hence we can simply return False without even considering the remaining matchsticks.

But, it turns out that we an save up on a lot of computation by looking to our good friend **Dynamic Programming**.

## Dynamic Programming based Solution

* In any dynamic programming based solution, what's important is that our problem must be breakable into smaller subproblems and also that these subproblems show some sort of overlap which we can save upon my caching results after computing them once and then reusing them on every repetitive call.

* Consider the following set of matchsticks that have been used already to construct some of the sides of our square (**Note:** not all the sides may be completely constructed at all times.)

```
3,3,4,4,5,5
```

* If the square side was `8`, then there are multiple possibilities for how many sides can be constructed using the matchsticks above. We can have

  ```
  (4, 4), (3, 5), (3, 5) -----------> 3 sides fully constructed.
  (3, 4), (3, 5), (4), (5) ---------> 0 sides completely constructed.
  (3, 3), (4, 4), (5), (5) ---------> 1 side completely constructed.
  ...
  ```
* As we can see above, there are multiple possibilities to use the same set of matchsticks and land up in completely different recursion states.

* This means that if we just keep track of what all matchsticks have been used and which all are remaining, it won't properly define the state of recursion we are in or what subproblem we are solving. A single set of used matchsticks can represent multiple different unrelated subproblems and that is just not right.

* An additional variable is required here to properly define our subproblems at a much more finer granularity. This variable is the number of sides formed completely. This variable can take on 4 different values according to the question since we have to form a square and the square would have 4 sides in all.

* Also, an important thing to note in the example we just considered was that if the matchsticks being used are `3,3,4,4,5,5` and the side of the square is `8`, then we will always consider that arrangement that forms the most number of complete sides over that arrangement that leads to incomplete sides. Hence, the optimal arrangement here is `(4, 4), (3, 5), (3, 5)` with 3 complete sides of the square.

* Let us take a look at the following recursion tree to see if in-fact we can get overlapping subproblems.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/matchsticks_diag-2.png)

* Clearly we have subproblems that overlap and hence we can apply dynamic programming to solve this problem.

* Now, we know that the overall sum of these matchsticks can be split equally into 4 halves (if not, we would not be solving that test case and would have simply returned False).

* The only thing we don't know is if 4 equal halves can be carved out of the given set of matchsticks. For that also we need to keep track of the number of sides completely formed at any point in time. ***If we end up forming 4 equal sides successfully then naturally we would have used up all of the matchsticks each being used exactly once and we would have formed a square***.

* Let us first look at the pseudo-code for this problem before looking at the exact implementation details for the same.

  ```
  let square_side = sum(matchsticks) / 4
  func recurse(matchsticks_used, sides_formed) {
      if sum of matchsticks_used % square_side == 0, then {
          sides_formed++
      }

      if sides_formed == 4, then {
          Square Formed!!
      }


      for match in matchsticks available, do {
            add match to matchsticks_used

            let result = recurse(matchsticks_used, sides_formed)

            if result == True, then {
                return True
            }

            remove match from matchsticks_used
      }
  }
  ```

* This is the overall structure of the dynamic programming based solution we will look at a few paragraphs from now. Of-course, a lot of implementation details are missing here that we will address now.

### Implementation Details

* It is very clear from the pseudo-code above that the state of a recursion is defined by two variables `matchsticks_used` and `sides_formed`. Hence, these are the two variables that will be used to **memoize** or cache the results for that specific subproblem.

* The question however is how do we actually store all the matchsticks that have been used? We want a memory efficient solution for this.

* The most basic approach here would be to simply use an array to store the used matchsticks. This is not really an efficient way to go about because we would have to hash this array and the variable `sides_formed` (which is an integer) and hashing an entire array is not really an efficient approach. (I know, I know what the Python lovers are saying. It's easy to write but not really memory efficient.)

* If we look at the question's constraints, we find that the max number of matchsticks we can have are 15. That's a pretty small number and we can make use of that. All we need to store is which of the matchsticks from the original list of matchsticks have been used.

  ```
  We can use a Bit-Map for this
  ```

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/wow.png)

* Yes, a bit-map. We will use N number of bits, one for each of the matchsticks (N is at max 15 according to the question's constraints). Initially we will start with a bit mask of all 1s and then as we keep on using the matchsticks, we will keep on setting their corresponding bits to 0.

* This way, we don't have to hash an entire array. Instead we just have to hash an integer value whose boolean representation is our bitmask and the max value for this mask would be 2<sup>15</sup>.

### Do we really need to see if all 4 sides have been completely formed ?

* Another implementation trick that helps optimize this solution is that we don't really need to see if 4 sides have been completely formed.

* This is because, we already know that our original sum of all the matchsticks is divisible by 4. So, ***if 3 equal sides have been formed by using some of the matchsticks, then the remaining matchsticks would definitely form the remaining side of our square.***

* Hence, we only need to check if 3 sides of our square can be formed or not.

### How do I check if a side has been completely formed ?

* As described above, there's a variable called `sides_formed` that is being used to track how many complete square sides have been formed till a particular point in recursion. How does this value get updated ?

*  What we do is that we use the bit mask to find out the matchsticks used till now and we sum their value up. If their value is divisible by the side of our square, then we increment the number of sides formed variable. This is done at the start of every recursion and if at any point, the number of sides formed becomes 3, we return True.

* **Time Complexity** : `O(4 * N * 2<sup>N</sup>)` = `O(N * 2<sup>N</sup>)` because at max `2<sup>N</sup>` unique bit masks are possible and for each one of them (* 4) we iterate our original matchsticks array to sum up values of matchsticks used to update the `sides_formed` variable.

* **Space Complexity** : `O(N + 4 * 2<sup>N</sup>)` because N is the stack space taken up by recursion and `4 * 2<sup>N</sup>` is the max possible size of our cache for memoization.
