<p align="center">
<img src="../../Images/Hand-of-Straights.png" width="600">
</p>

To check if the cards can be rearranged in groups of `W` consecutive cards, we need to realize that every first card of each group should have their `W-1` consecutive cards in the hand of cards. The intuition behind this problem is that we sort our **unique** hand of cards and approach the problem greedily. Which essentially means finding the consecutive cards for the current smallest card of a group.

---
### Solution 1: Greedy Approach

#### Algorithm

* Find the consecutive cards for the current smallest card of a group.

* Once we are done with one group we move on to the next smallest card left in the hand of cards to form the next group. The program hence returns `True` if we have formed groups for all the small hands we encounter.

* Note that if we create a frequency counter for all the cards in our hand of cards and iterate the keys (i.e.) unique hands in increasing order we can achieve this in lesser time. We can check if we have enough next in line cards for the given hand. Which is the next W-1 cards.

* For eg. If we have to create a group of three hands and the current hand is `2` with a frequency of "4". It means we have four hands of `2` and we would need atleast four hands of both `3` and `4` to create a group of three hands `2,3,4`

* So if we do not have enough next in line consecutive hands, we return 1 `False`. Otherwise we check the same condition for next smallest hand which has a frequency > 0.

* If we are able to create groups for all the unique hands we return `True`.

#### Complexity Analysis

* Time Complexity: `O(NlogN)`
* Space Complexity: `O(N)`

#### Link to OJ

https://leetcode.com/problems/hand-of-straights/description/

---
Article contributed by [Sachin](https://github.com/edorado93) and [Divya](https://github.com/DivyaGodayal)
