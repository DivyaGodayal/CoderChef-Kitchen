# 2 Keys Keyboard

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/2-Keys.png)

At any point you can either copy or paste. We can solve this question recursively. Since we have to print a given number of A's in the minimum steps possible we need to come up with an optimal answer for each step of out recursion. 

And what if we save this optimal answer of everystep? -- MEMOIZE
We would save alot of overlapping computations and hence a Dynamic Programming solution is what we have to serve you today!

```
#Cache the answer    
memo[(rem, buf)] = ans
```            

To every recursive call we pass how many A's are still left to be printed and once we don't have anything to printing we hit the base case. 
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
In every recursion we can either copy to the buffer or we can paste from the buffer. 

### Copy and Paste 
If we copy to the buffer, now we have the copied current string to the buffer i.e. ```n-rem```. So we can perform the next paste operation together and add up two operation(+2)

```
# If new remaining is >= 0 i.e. if that many 'A's were actually left to be printed, then recurse
if new_rem >= 0:
    ans = recurse(new_rem, n - rem) + 2
```

### Paste
If we just paste then we just paste to the current string whatever is in the buffer.
```
# If the number of 'A's in the buffer are <= the number of 'A's left to be printed on screen i.e. rem., then recurse 
if buf > 0 and buf <= rem:
    ans = min(ans, recurse(rem - buf, buf) + 1)
```

**Out of the two operations above whatever gives a minimum answer(lesser steps) is the required answer for current recursion and is hence memoized and also returned to the previous step**


