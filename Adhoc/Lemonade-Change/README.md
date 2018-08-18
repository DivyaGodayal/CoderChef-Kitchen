![alt text](https://raw.githubusercontent.com/DivyaGodayal/CoderChef-Kitchen/master/Images/Lemonade-Change.png)

## SOLUTION

* This problem demands a basic greedy approach all of us follow in our day to day life.
`Let me save the change, I might need it later`.

* Consider a basic scenario. 
`You have two $5 notes and one $10 notes.`

You go to the market and buy an energy bar for $10. 

How would you pay?

Credit Card. LOL. 

No. You are not carrying that. You just have two $5 and one $10 notes. 

If you are like me, you would give the $10 note and keep those two $5 notes for later.

`Why? Because...`

So now you want to have a cup of green tea which would cost $5 and the tea vendor has a board outside his shop which says **Only $5 notes accepted.** Now, in this case you need to have those two $5 notes. Had you given the two $5 notes earlier for the energy bar, you would not have been able to have the delicious green tea :P

* This is all this questions wants. Be greedy! 

* You just have to deal with $5, $10, $20 notes. Since $20 is the highest currency note it won't be utilized as a change.

* You just keep a count of $5 and $10 notes you have at any point in time. 

* If you are able to provide the change from your current notes collection, you return True, otherwise False.

* Scenarios you might face:
  1. The customer comes in with a `$5` note. In that case you just add it to your collection. `Five-Dollar-Notes + 1`
  2. The customer comes in with a `$10` note. In that case you need to return $5 to the customer. You check if you have a $5 note, if you do, then you take it out from your collection and give it to the customer. Also add the $10 to your collection. `Five-Dollar-Notes - 1` and `Ten-Dollar-Notes + 1`
  3. The customer comes in with a `$20` note. In that case you need to return $15 to the customer. Now you could either give back `one $10 and one $5` or `three $5`. If you are smart, you would first try the former option. Since you would want to reserve the $5 notes for later use. Also you don't add $20 to your change collections, Since you can't exchange it for any other transaction. So you either do (`Five-Dollar-Notes - 1` and `Ten-Dollar-Notes - 1`) or `Five-Dollar-Notes - 3`.

* **Time Complexity** O(N), where N is the length of bills.

* **Space Complexity**: O(1). 
