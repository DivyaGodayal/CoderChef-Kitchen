Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].


##SOLUTION

* The solution to this problem uses a heap based greedy approach. So the basic idea is that we count the frequencies of all the elements of the given string and then we create a max-heap for these characters along with their frequencies.
* Now that we have the heap, we pop an element, add it to our resulting string, reduce it's frequency and we keep repeating until all the characters in the original string have been accounted for. 
* Say the frequencies were as follows 'a':2, 'b':1. Now if we pop the first element from the heap, we get 'a':2 and after adding 'a' to our resulting string we get 'a':1. Now if we add it back immediately, it is possible that the heap will give us 'a':1 right back at the next pop operation. This would lead to violation of the condition that no two character should come side by side. 
* Therefore, after adding a character to the resulting string, we hold on to it and only add it back once the next character has been added to the resulting string. So for our example, we will only add 'a':1 back to the heap once 'b':1 has been popped and added to the resulting string. 
