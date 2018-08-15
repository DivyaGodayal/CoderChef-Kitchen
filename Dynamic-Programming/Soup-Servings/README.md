![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Soup-Servings.png)

## SOLUTION
* This problem is a dynamic programming problem. You come to that conclusion once you realize there will be overlapping solutions. 
So for a given set of soup serving quantities (A, B) after performing the operations it might lead to repeated nodes/states. And for huge values of A and B the number of repeated states would be lot more. Hence we need Dynamic Programming i.e. saving the answers for a given (A, B) so that if you come across the same set of soup servings(A, B) we don't need to repeat the computation.

* Lets say this is a real world scenario. You are the chef and you need to serve the soup and you are asked to solve this problem. How would you solve this? You would probably think let me serve it and see. But that essentially means you follow a set of operations and the soup is already over. 
What now? No more soup to try other operations?
Thats when you let DP, go through all the combinations.

* The solution is recursively doing the four operations needed.
`	Serve 100 ml of soup A and 0 ml of soup B
	Serve 75 ml of soup A and 25 ml of soup B
	Serve 50 ml of soup A and 50 ml of soup B
	Serve 25 ml of soup A and 75 ml of soup B
`

* Whatever these four calls return is multiplied by 0.25 since we have a probability of 0.25 for every operation.  

* **Base Case**: If at any point `A empties before B` or `A and B both empty together`, then we return a 1 probability corresponding to that operation from this call. Otherwise we return a 0.

Refer to the solution. Its easy peasy!
