![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Task-Scheduler.png)

## SOLUTION

* The solution to this problem uses a heap based greedy approach. So the basic idea is that we count the frequencies of all individual tasks in the list of given tasks and create a Max heap using those.

```
For eg. tasks = ["A","A","A","B","B"] , n = 2 
```

```
The heap created would be (A,3)-(B,2)
```

* Now that we have the heap, we pop an element until the heap finishes or until n+1 elements have been popped. n being the interval. 

```
No of elements to be popped is n+1 = 3
But, Heap size = 2, Hence number of elements popped = 2
```

* The frequencies of the elements being popped are reduced by one and kept in an interim list so that a given task is not repeated before n+1 intervals. 

```
Interim List = (A,2)-(B,1)

Since we just popped 2 elements, there is still one interval left to satisfy our condition of no repitiion of tasks.

This interval has to be idle.
Hence 3 Intervals Occupied
A -> B -> IDLE
```

* Hence the interim list elements are pushed back once you have all the n elements for the n intervals. 

```
After pushing the elements back, Heap elements now (A,2)-(B-1)
```

* Max heap on frequencies ensures that maximum frequency elements occupy the starting position of the n intervals and lower frequency elements occupy the later positions or if there are not enough elements left to fill the n intervals the CPU can sit idle. 

```
For eg. in the next iteration, Interim list = (A,1)
Next 3 intervals would be 
A -> B -> IDLE
```

* Note, the number of steps is always (n+1) except in the last stretch. 
* For the last stretch, since there are no further elements left, there is no need for the CPU to sit idle after completing the job in hand.
Hence the last set would just be the number of final tasks popped.

```
After the last push, Heap elements are (A,1)
After Popping the elements, Interim List is (A,0)
A ->
```

```
Solution to ["A","A","A","B","B"] , n = 2 

7 intervals 

	Here is how:
	3 intervals - A -> B -> 
	3 intervals - A -> B -> IDLE
	1 interval - A -> 

