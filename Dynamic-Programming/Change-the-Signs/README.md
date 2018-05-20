
![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Change-the-signs.png)

We are given a sequence of numbers and we have a certain operation we can perform on them. The operation is that we can negate some (possibly none) subsequence of numbers from the given list. So eg:- Let us consider this following list of numbers

```
4, 3, 1, 2
```
Now, negating a subsequence would give us multiple possible arrays. Like 

```
4 3 1 2 (We did not negate anything here. This is a valid subsequence)
-4 3 1 2
4 -3 1 -2
4 3 -1 2
4 3 1 -2
-4 -3 1 2 etc.
```
Not all of these are valid, however. The valid subsequences are the ones where **no substring  having length > 1 has a negative sum**. Let's see what all subsequences were valid from the ones mentioned above.

```
4 3 1 2 VALID
-4 3 1 2 INVALID
4 -3 1 -2 INVALID
4 3 -1 2 VALID
4 3 1 -2 INVALID
-4 -3 1 2 INVALID
```

As you can clearly see, we only have 2 valid subsequences that can be obtained  by performing the operation mentioned above. **Note:** we haven't written down all the possible subsequences. That would be 2^n i.e. 16 in this case because for every number we have two options. Either to negate it, or not.

Now the 2 valid set of numbers are `4 3 1 2` and `4 3 -1 2`. We need to return the set that has the **MINIMUM OVERALL SUM** which would be `4 3 -1 2` in this case. 

## Dynamic Programming 

This problem can be solved by dynamic programming and is divided into two basic parts. 
* One is the main dynamic programming recursion that we use to find out the **minimum sum of the final set**. Note, the dynamic programming is not directly used to obtain the final set, just the final sum of the set. So our dynamic programming approach would correctly find out the sum for the example given above as 8. `4 + 3 + (-1) + 2 = 8`. 
* What we actually need is the final modified set of numbers where some (possibly none) of the numbers are negated. We use the concept of a **parent pointer** and backtracking to find out the actual set of numbers. 

Let's move onto our recursion relation for our dynamic programming approach. 
Before describing the recursive relation an important observation to make here is that if a number has been negated, **then any adjacent number to it can not be negated** i.e. two adjacent numbers cannote be negated as that would give a substring of length 2 whose sum is negative and that is not allowed according to the question. 

For the recurrence relation, we need two variables. One is the index number of where we are in the array and one is a boolean value that tells is if the previous number (one left to the previous number) is negated or not. i.e. if the current index is `i` , then the boolean value would tell us if the number at `i-2` was negated or not. You will know the importance of this boolean variable in the next paragraph. 

We need to know in `O(1)` if a number **can** be negated or not. Since we are following a recursion with memoization based solution, whenever we are at an index `i` in the recursion, we are sure that the numbers to the right i.e. `i+1` onwards have not been processed till now meaning that all of them are still positive. 

The choice of if the number at index `i` can be negated is dependent upon the right hand side (if there is one) and the left hand side (if there is one). The right hand side is easy. All we need to check is if 

``` number[i] < number[i + 1]``` because if this is not true, then adding these two would give a negative value for the substring `[i, i+1]` thus making it invalid. 

Now comes the tricky part. We need to see if negating the number at `i` will cause a substring of negative sum or not. When we reach the index `i` in our recursion, we have already processed the numbers before it and some might have been negated as well.  So say we have these set of numbers `4 1 2 1` and we had negated the first `1` and we are now processing the last number i.e. `1` . 

``` 4 -1 2 [1]``` The last number in the square brackets is the one we are processing. We cannot apply the following approach here directly 

``` number[i] < number[i - 1]``` because `1 < 2` but if we negate that last 1 as well, we will have `4 -1 2 -1` and the sum of the substring `-1 2 -1` won't be **positive** which is a violation. So simply applying this check won't work. 

Here comes in the boolean variable which tells us if, given an index `i`, if the number at `i - 2` was negated or not.  Consider the two scenarios. 

* Yes, the number at index `i - 2` was negated. In that case, negation of the number at `i - 2` would have a capacity reduction for number at `i - 1`. In the example `4 1 2 1`, negating the 1 at index 2 (1 based indexing) would reduce the capacity of the number 2 (at index 3) by 1. I refer to remaining values of numbers as capacities here. We need to consider this reduced capacity when performing the check. 

	``` number[i] < remainingCapacity(i - 1)```

* In case the number at `i - 2` wasn't negated, then the number at `i - 1` can be used directly as ``` number[i] < number[i - 1]```. 

Consider the pseudo-code-ish for a better understanding of the recursion. 

```
def recurse (index, was_prev_negated) 
{
	# No number left to process
	if index == N:
		return 0
	
	# If we keep the number at index i positive only. 
	keep_positive = recurse(index + 1, false) + numbers[i]
	
	right_check = (i == N - 1	or numbers[i] < numbers[i + 1])
	if 	was_prev_negated == True:
		left_check = numbers[i] < (numbers[i-1] - numbers[i-2])
	else:
		left_check = numbers[i] < numbers[i-1]	
	
	if left_check and right_check:
		# We are adding the negated value of (i) and positive value of 
		# index i+1 and we jump to recurse on i+2. We cannot have 
		# two negative numbers side by side. So if i was negated, then
		# i + 1 must be positive. 
		keep_negative = recurse(i + 2, true) + (-numbers[i]) + (i < numbers.size() - 1 ? numbers[i + 1] : 0)

		return min(keep_positive, keep_negative)
}
```

Now that we have the recursion in place, we simply need to memoize. As for memoization, it is as simple as 

``` memo[i][was_prev_negated] = min(keep_positive, keep_negative)```

All this is fine dandy, but the question asks us to actually print the final set of numbers that gives the minimum sum after making such modifications. For that, we need to use a parent pointer that would tell us at every index and boolean variable `was_prev_negated`'s value as to what optimal action was taken. 

```parent[i][was_prev_negated] = min(pos, neg) == pos ? 1 : -1```

So we simply store 1 or -1 depending upon if we chose to negate the number at the index i or not. 

## Backtracking

Now comes the part where we backtrack to find the solution to our original problem. Note, the decision for the very first number is what propagates the recursion further. i.e. if the first number was negated, the second number would be positive and the third number's decision can be found using `parent[2][true]`. Similarly, if the first number wasn't negated, then we move onto the second number and it's decision can be found using `parent[1][false]` and so on. Look at the pseudo-code-ish

```
def retrace(was_first_number_negated):
	start = 1
	was_prev_negated = was_first_number_negated
	if was_first_number_negated == True:
		print (-1 * numbers[0])
		start = 2 # Note, we have to skip one number here.
	else:
		print numbers[0]

	for i in start..N:
		if parent[i][was_prev_negated] > 0:
			was_prev_negated = false
			print (numbers[i])	
			i += 1
		else:
			was_prev_negated = true
			i += 2 # Again, we have to skip. 
			print (-1 * numbers[i])
			
			# i could've been the N - 1 i.e. the last number.
			if i < N - 1:
				print numbers[i + 1] # We know for sure this would be positive if ith index was negated.

```
## Better Approach
This problem could even be solved by 1 Dimensional DP.
Instead of checking for the capacity check on the left side, we can look foward. 
Which simply means if you are at an index, you check if that element along with the element at index+2 have the capacity to swallow the element at index+1. If there is a possibility of swallow then we directly jump to index+3, if we negate element at index because element at index+1 and index+2 both can't be negative.

---
```
SWALLOW POSSIBLE 
4,[1],2,1,3,1,2
```
**Left, Right and Swallow check satisfied at index = 1**
If we negate the element at index = 1 i.e.[1], we can't negate
elements at 
```
index = 2 
4,-1,-2,1,3,1,2 \\INVALID
```
```
index = 3 
4,-1,2,-1,3,1,2 \\INVALID \\LEADS TO SWALLOW OF INDEX = 2
```
Hence we jump to index = 4

---
```
SWALLOW NOT POSSIBLE 
4,[1],3,1,3,1,2 
```
If the swallow is not possible then we jump to index = 3.

```
index = 3 
4,-1,2,[1],3,1,2 //Still valid
```
---

Below is a small snippet from the code for the above condition. Please check the solution provided to understand things better. 

```
 if right_check and left_check > 0:
        if swallow_check:
            neg = recursive_signs(index+3) - A[index] + A[index + 1] + A[index + 2]
        else:
            neg = recursive_signs(index+2) - A[index] + A[index + 1]

```

Bactracking has a similar change, we look forward instead.

Since at any point we are looking forward and jump to the index only if its a possible canditate for negatition in that particular recursion we save ourselves from keeping an extra recursion variable - ```was_prev_negated```

Hence just one recursion variable i.e. the current index.
