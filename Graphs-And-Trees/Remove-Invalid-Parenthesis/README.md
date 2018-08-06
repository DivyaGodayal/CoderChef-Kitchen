![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/invalid-paren.png)

* The problem statement is self explanatory. 
* We need to remove **_minimum_** number of parenthesis from the given expression
to make the resulting expression a valid one. 
* A valid expression would have **_balanced set of left and right parenthesis_**

## A Recursive Naïve Solution

* There is a very simple recursive approach to this problem. 
* The question asks us to remove some (maybe even 0) parenthesis to make the resulting 
expression valid. 
* Since we don't really know which of the parenthesis should be removed, we can 
**_try all possibilities_**. 
* That's like the basis of every recursive approach. To try out all the possibilities and 
see which of them works and end up giving us the optimal solution. 
*  The question also asks us to find out `all possible resulting expressions.`. It is 
clear from one of the examples given in the question that we may end up 
with multiple resulting expressions after removing the so called **minimum invalid parenthesis**.
* Here is the pseudocode for this approach. 

```
func remove_invalid(expression) {
    if (end of string reached), then {
        if (resulting expression is valid) {
            let N = number of parenthesis ignored
            if (N == current minimum) {
                record this resulting expression in a set (no duplicates)
                
            } else if (N < current minimum) {
                set current minium = N
                re-initialise the answer set to contain the resulting expression only.
            } 
        }
    }
    
    if (current_character in the original expression not one of '(' and ') ){
        --> Recurse one step ahead. No removals required here. 
    }
    else {
        --> Recurse without removing the current parenthesis.
        --> Recurse after removing the current parenthesis. 
    }
``` 

* This is a truly exhaustive algorithm and this does indeed poorly on the leetcode overall 
set of submissions faring in the last 2% of the solutions only and this 
takes a whooping **1752ms** to pass all the test cases. 

* **Time Complexity:** O(2^n) because for every parenthesis we can either consider it or remove it and 
accordingly we have two recursions. Time spent once the recursion is over to add to the solutions set etc. is considered
to be O(1) although it is not. 
* **Space Complexity:** O(2^n) because of the recursion stack.

## Intelligent Recursive Solution

* Let us take an insight from the previous approach on the improvement that 
we would look at now. 
* In our previous approach we look at **ALL** of the possibilities i.e. 
we try removing each of the parenthesis and in the end we check if the resulting 
expression is even valid or not. 
* This means we would have recursions where we end up ignoring so many 
parenthesis that were in fact not to be ignored. 
* What we should be doing instead is to only remove as many number of left and 
right parenthesis as there are invalid left and right ones. 

* For e.g. we found out that there are 3 misplaced left and 3 misplaced 
right parenthesis in the entire string and the overall string contains 500 
left and 500 right parenthesis, then we won't end up removing more than 
3 left or right parenthesis and this would bring down the number of possibilities 
we try drastically thus reducing the overall time.      

* Let us look at the pseudo-code for finding out the number of misplaced left and 
right parenthesis first. 

```
func find_misplaced_paren(expression) {
    let left = 0
    let right = 0
    for every character in the expression {
        if (character == '('){
            left ++
        } else {
            if left > 0 {
                left --
            } else {
                right ++
            }
        }
    }
}
```

* This will give us the number of left and right parenthesis that are supposedly 
misplaced. This won't obviously tell us which ones though. That is what the actual 
recursion is for. 

*  The only change that we make to our previous recursive approach is that now we 
only consider removing a parenthesis if the number of misplaced parenthesis of 
that type is > 0. Otherwise we don't remove it because we would have already 
exhausted our count of invalid parenthesis and removing any more would 
anyways lead to an invalid expression in the end. 

* Also, in our previous approach we had to check if the number of removals we 
have done till now is the minimum or not and update the answer set accordingly. 

* This is something that is not necessary here because the counts in `left` and `right`
tell us the minimum number of removals to be done to achieve a valid expression. So, 
any valid expression that we get at the end of our recursion will anyways be a valid one and 
that too achieved by removing the minimum possible parenthesis. 

* **Time Complexity:** O(N<sub>C<sub>(left + right)</sub></sub>) because that is number 
of possibilities we need to examine. We can have any of the `left + right` parenthesis removed 
out of the possible N in the entire string. 

* **Space Complexity:** O(N<sub>C<sub>(left + right)</sub></sub>)