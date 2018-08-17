![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Lemonade-Change.png)

## SOLUTION

* This problem demands a basic greedy approach all of us follow in our day today life or atleast our mothers do.

`Let me save the change for later, when I would need it`.

* Consider a basic scenario. 
`You have two $5 notes and one $10 notes.`

You go to the market and buy an energy bar for $10. 

How would you pay?

Credit Card. LOL. No. You are not carrying that. You just have two $5 and one $10 notes. 

If you are like my Mom you would give $10 note and keep those two $5 notes for later.

`Why? Because...`

So now you want to have a cup of green tea which would cost $5 and the tea vendor has a board outside his shop **Only $5 notes accepted.** 

* This is all this questions wants. Be greedy! 

* You just have to deal with $5, $10, $20 notes. Since $20 is the highest currency note it won't be utilized as a change.

* You just keep a count of $5 and $10 notes you have at any point in time. 

* If you are able to provide the change from your current notes collection you return True, Otherwise False.

* Scenarios you might face:
  1. The customer comes with a `$5` note. In that case you just add it to your collection. **Change Collection Update** `+($5)`
  2. The customer comes with a `$10` note. In that case you need to return $5 to the customer. You check if you have a $5 note, if you do then you take it out from your collection and give it to the customer. Also add the $10 to your collection. **Change Collection Update** `-($5)` `+($10)` 
  3. The customer comes with a `$20` note. In that case you need to return $15 to the customer. Now you could either give back `one $10 and one $5` or `three $5`. If you are smart you would first try the former option. Since you would want to reserve more $5 notes for later use. 
  Also you don't add $20 to your change collections, Since you can't exchange it for any other transaction. 
  **Change Collection Update** So you either do `-($5)` `-($10)` 
  or  three times `-($5)`.

* **Time Complexity** O(N), where N is the length of bills.

* **Space Complexity**: O(1). 
