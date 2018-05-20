## SOLUTION

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/2-Keys.png)

So according to the question we have to print a certain number of 'A's on the screen and we have just two operations with equal cost at our disposal.At any point you can either copy or paste. We can solve this question recursively. The reason for that is that once we have printed say X number of 'A's on the screen optimally, we need to decide the optimal set of steps for the remaining number of 'A's i.e. (N - X) and that in itself is a subproblem of what we wanted to solve initially. Hence the recursion.

To every recursive call we pass how many A's are still left to be printed and once we don't have anything to left to be printed, we hit the base case.
```
 if rem == 0:
 	return 0
 ```
Recursive Call - ```recurse(remaining , buffer )```

```
n = Total number of A's needed
rem = remaining A's at any point of recursion
new_rem = new remaining after every paste
buff = buffer
```
In every recursive call,  we can either copy to the buffer or we can paste from the buffer. Take a look at the following example for clarity.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/2-Keys-Recursion.png)

### Copy and Paste
If we copy to the buffer, now we have the copied current string to the buffer i.e. ```n-rem```. The next operation definitely needs to be a paste operation and so the number of operations perfomed because of this copy are +2.

```
# If new remaining is >= 0 i.e. if that many 'A's were actually left to be printed, then recurse
if new_rem >= 0:
    ans = recurse(new_rem, n - rem) + 2
```

### Paste
If we just paste then we just perform this single operation where we print to the screen whatever we had in our buffer.
```
# If the number of 'A's in the buffer are <= the number of 'A's left to be printed on screen i.e. rem., then recurse
if buf > 0 and buf <= rem:
    ans = min(ans, recurse(rem - buf, buf) + 1)
```

Out of the two operations above whatever gives a minimum answer i.e. lesser steps to reach the desired number of A's is the required answer for current recursion and gets returned to the previous step and also gets cached for the next time.

A problem with this solution is that of repeated computations. Meaning that if we plot the recursive graph for this recursive relation defined above we would see that there are subproblems being repeated. Take a look for yourself.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/2-Keys-DP.png)

The yellow circles represent repetition of states.

What could we do ?

What if we save this optimal answer of every step? -- MEMOIZE
We would save a lot of overlapping computations and hence a Dynamic Programming solution is what we have to serve you today!

```
#Cache the answer    
memo[(rem, buf)] = ans
```            

**Time Complexity**:  The time complexity of any recursive solution is always dependent upon what variables define its state and if that state is cached or not and also the computation taking place per recursive call. So in our case, the states are cached meaning they are always visited once and the state is defined by the two variables remaining and buffer and also there is O(1) i.e. constant time operation being performed pr recursive call. The total number of states possible are (remaining * buffer).Maximum value for remaining is O(n) and that for buffer is also O(n) and hence the time complexity is **O(n^2)**

**Space Complexity**: Space complexity in recursive calls is defined by the number of recursive calls because that is the space occupied by the recursive stack .Also the space occupied by the caching dictionary if any adds to the space complexity. So, the space complexity here is **O(n^2) + O(n^2)** which is essentially **O(n^2)**.
