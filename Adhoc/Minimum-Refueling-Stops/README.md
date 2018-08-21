![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Minimum-Refueling-Stops.png)

## SOLUTION

**Dynamic Programming Approach:**

* This problem is similar to increasing subsequence, in the way that we look back to the previous dp elements to calculate the present one. 

Lets define dp[i]:
`dp[j] -  the farthest location we can get to using j refueling stops.`

If dp[2] = 200 miles, this means we can reach 200 miles by refueling at 2 stations.

* We need to reach the target in the minimum number of steps/stations. Hence, we want the smallest i for which dp[i] >= target. 

* We visit each station in order. For every station we check the dp array moving backwards from the current index. 
If the value of the current dp cell `dp[j]` indicates that its reach is equal to or beyond the current station's location `stations[i]`, this means with j stations the car can reach station i. Hence we add the current stations fuel to dp[j].

`Stations[i][1] = Fuel at Station i.
dp[j+1] = max((dp[j] + Stations[i][1]), dp[j+1])
dp[j+1] = the farthest location we can get to using j refueling stops.
`

* This means we are adding a station[i] = (location, capacity), any time we could reach this station with j refueling stops, we can now reach capacity further with j+1 refueling stops.

For example, if we could reach a distance of 200 miles with 2 refueling stops, and now we added a station at location 100 with 50 liters of fuel, then we could potentially reach a distance of 250 miles with 3 refueling stops.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Minimum-Refueling-Stops-DP.png)

* **Time Complexity** O(N^2), where N is the number of stations.

* **Space Complexity**: O(N), the space used by dp.


**Max-Heap Approach:**

* This approach is easier to understand.

* The questions just asks us to calculate the number of minimum stations we need to stop at to refuel the car to reach the target.

* The best thing about this problem is that its not reality. And so we don't have to take our decision promptly. We don't have to take a decision of choosing to refuel the car while actually crossing the station in the car. 

* So, this is what we do. We drive to whatever maximum we can, while keeping a track of all the stations that came along. 

* Once the fuel gets over we greedily pick from the stations we crossed. Picking up the station which has the maximum fuel. 

* This process could be repeated till we hit the target.

* To maintain a list of stations which came on the way, we can use a max heap. So whenever we run out of fuel we can pop the top element from the heap. The number of pops is the number of stations we need to stop at to refuel.

* If we never hit the target sum then we return -1.

![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Minimum-Refueling-Stops-Heap.png)

* **Time Complexity** O(NlogN), where N is the number of stations. 

* **Space Complexity**: O(N), the space used by heap. 
