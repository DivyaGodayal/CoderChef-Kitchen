![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/daily-temp.png)

## Solution

* We are given a list of temperatures over multiple days , we are to 
find, for every individual day, after how long will a warmer day arrive. 

* If you think about these temperatures as just numbers, then what we have to 
do here is: Given a list of numbers, for every number find out the index of the next
higher element in the list. That's all we have to do to solve this question.

* We don't need to report the actual index of the next larger element, we need to 
report the distance of that index from the current index. 

* This classic problem can be solved by two different data structures
    1.  Heap
    2. Stack
    
### Heap based Solution

* So, the idea here is very simple. We keep on iterating on the list of 
numbers in the forward direction and we do the following for each element.

* For every element, we pop all smaller elements from the heap. The current element
will act as the next higher element for all of these smaller elements that 
are there in the heap. Note: if this was not the case and some previous index would 
have been the next larger element for some of these elements in the heap, then
they would not be there in the heap in the first place at this point. 

* After removing all the smaller elements from the heap and assigning their 
next largest element properly, we add the current element to the heap and we 
move forward. 

* **Time Complexity**: `O(nlogn)` we eventually push and pop every element from the heap.
* **Space Complexity**: `O(n)` for the heap      

## Stack based solution

* It turns out that we can do better on this task complexity wise by using the 
stack data structure. 

* We iterate on the array in reverse. 

* For every element we do these steps:
    1. Pop all the elements from the stack that are smaller than this element 
    or until the stack doesn't become empty. 
    2. If we found an element that was larger than this element, then that
    element on the stack would be the next larger element corresponding to the
    current element. 
    3. If the stack became empty, then this current element is the largest one
    till now. 
    4. Add the current element to the stack and repeat the process.
    **Note:** we are moving in the reverse direction on the array for this to work.
    
* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`    

### Dry Run

* Let us try and dry run the stack based algorithm on the following example. 

* A slight modification to the algorithm described above, we add the element's index to the stack and 
not the actual element because the question asks us to print the number of days 
till the next warmer day.

```
[75, 69, 72, 76, 73]
 <-----------------
 
 * i = 4, element = 73, stack = []
    --> add 4 to the stack as stack is empty.
    --> next_largest[4] = 0
 
 * i = 3, element = 76, stack = [4]
    --> Pop until stack empty or larger element found.
    --> element > temperatures[stack[top]], therefore stack.pop()
    --> next_largest[3] = 0
    --> add 3 to the stack    
 
 * i = 2, element = 72, stack = [3]
    --> element < temperatures[stack[top]]
    --> next_largest[2] = stack[top] - 2 = (3 - 2) = 1
    --> add 2 to the stack
    
 * i = 1, element = 69, stack = [2, 3]
    --> element < temperatures[stack[top]]
    --> next_largest[4] = stack[top] - 1 = (2 - 1) = 1
    --> add 1 to the stack
    
 * i = 0, element = 75, stack = [1, 2, 3]
    --> Pop until stack empty or larger element found. 
    --> element > temperatures[stack[top]], therefore stack.pop()
    --> element > temperatures[stack[top]], therefore stack.pop()
    --> element < temperatures[stack[top]]
    --> next_largest[0] = stack[top] - 0 = (3 - 0) = 3
    --> add 0 to the stack
```

```
next_largest = [3, 1, 1, 0, 0]
```