https://www.codechef.com/MAY18B/problems/FAKEBS

## SOLUTION

The only thing the Chef can do is to preprocess the array by swapping some pair of numbers here and there so that the binary search procedure still returns the right index.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Fake-BS-diag1.png)

Note: The preprocessor above should ideally return the modified array for the binary search to work correctly. However, as the problem statement asks, we are just trying to determine the number of swaps needed for binary search to work correctly on the unsorted array given an input. The algorithm would also return a -1 if such a modification is not possible for the given array and element.

The idea here is very simple.

We need to understand two basic steps. I call them the **TI-ME** steps. Perhaps that’ll help you remember what we are doing here.

a. **T**arget **I**ndex: The index of the element to be searched for. We need to know this, since this index would help us drive the modifications. Because every time we modify any element, we need to sail towards this index and not away from it.

b. **M**iddle **E**lement: If you look clearly in a binary search, it’s the middle element of the current search space which drives the next move. If this middle element takes us in the wrong direction, we need to replace with the appropriate element.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Fake-BS-diag2.png)

We are searching for 8 in the above unsorted array. We already saw in the examples above a normal binary search would fail for an unsorted array.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Fake-BS-diag3.png)

Mid elements give direction to binary search. Middle element 5 would take binary search to go right. This way we would never find 8. If we swap 5 with an element greater than 8 we would force the search to go to left.

So, the whole idea here is that we swap all the middle elements which are wrongly placed.

The binary search algorithm (the value of the middle element with respect to the element to be searched, that is, X) can either take us towards the left half of the array or the right half. So, there are two possibilities for a wrongly placed middle element:

1. The element to be searched was on the right of the middle element, but since `Element[Mid] > Element[Target Index]` , the binary search would have had to ignore the right half and move towards the left half. OR

2. The element to be searched was on the left of the middle element, but since `Element[Mid] < Element[Target Index]` , the binary search would have had to ignore the left half and move towards the right half.

Therefore, if a middle element is wrongly placed such that a number X was needed in its place where `X < Element[Target Index]` , then we maintain a counter for that and call it `count_low_needed` .

Similarly, if a middle element is wrongly placed such that a number X was needed in its place where `X > Element[Target Index]` , then we maintain a counter for that and call it `count_high_needed` .

Also, if we simply run the binary search algorithm over the given array while searching for numbers, there would be some numbers that would be correctly placed. These would be the middle elements that drove the binary search in correct directions corresponding to the given element `X` (the element to be searched). These numbers cannot be a part of the swapping, because they are rightly positioned with respect to `X` .

Let’s look at the pseudo code for this algorithm first and then go through an example.

```

	function can_preprocess(arr, X)
	{
	     low = 0
	     high= 0

	while X is not found {
	          mid = (low + high) / 2
	          if arr[mid] == X {
	             break           
	          }

	correctly_placed_low = 0
	          correctly_placed_high = 0
	          count_low_needed = 0
	          count_high_needed = 0

	if `mid` suggests we should go right for X {
	               if X is actually on the right {
	                   correctly_placed_low ++
	               }
	               else {
	                   count_low_needed ++
	               }
	          } else {
	               if X is actually on the left {
	                  correctly_placed_high ++
	               } 
	               else {
	                  count_high_needed ++
	               }
	          }

	modify low and high according to 
	          where `X` actually is with respect to `mid`

	}

	// Total smaller numbers available for swapping
	     TSM = sorted_index[X] - correctly_placed_low

	// Total Larger numbers available for swapping
	     TLM = (N - sorted_index[X]) - correctly_placed_high

	if count_low_needed > TSM or count_high_needed > TLM {
	          return -1
	     }

	return max(count_low_needed, count_high_needed)

```

**NOTE:** The problem statement fixes the input array for us and repeatedly passes values to be searched in the input array. So, we can iterate once over the original array to know the actual location of the element to be searched (create a dictionary, essentially).

Also, we need `sorted_index[X]` to tell us how many values are lesser than or greater than the element `X` in our array. We can sort the array and create another dictionary storing location of each element in the sorted array.

Let’s go through the steps of the proposed algorithm while dry running an example.

1. Given an unsorted array, you need to search for `X = 4` .
    Hence our target index is 7.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Fake-BS-diag4.png)

2. Mid element index < Target Index, so we need to maneuver our search to the right half. But `Element[Mid] > Element[Target Index]`, hence `count_low_needed = 1`.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Fake-BS-diag5.png)

3. Mid element index < Target Index, so we still need to maneuver our search to the right half. Once again, `Element[Mid] > Element[Target Index]`, hence `count_low_needed = 2`.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Fake-BS-diag6.png)

4. The total number of swaps needed for binary search to return the correct index here would be two swaps with elements lower than 4. We have smaller numbers `1, 3 or 2` for swapping available, so we can successfully do the swapping for this array so that binary search correctly finds out `4` .

The time complexity of this Fake Binary Search algorithm is still `O(nlogn)` .