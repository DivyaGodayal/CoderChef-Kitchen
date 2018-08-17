class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # If no bills then return True
        if len(bills) == 0:
            return True
        
        # keep the count of $5 and $10 notes.
        count_fives = 0
        count_tens = 0
        
        # For each bill
        for bill in bills:
            # If the customer gave $5 then just increase the count of $5 notes by 1.
            if bill == 5:
                count_fives += 1
                continue
            elif bill == 10:
                if count_fives > 0:
                    # If you have $5 notes to return, just decrease $5 count by 1 and increase $10 by 1.
                    # Since we returned $5 note to customer and took $10 from him.
                    count_fives -= 1
                    count_tens += 1
                else:
                    # Otherwise we do not have $5 change to return to the customer, return False
                    return False     
            else:
                # If we have $5 and $10 notes to return a sum of $15 then return true.
                if count_fives > 0 and count_tens > 0:
                    count_fives -= 1
                    count_tens -= 1
                elif count_fives > 3:
                    # Otherwise, If we just have enough $5 notes alone to return a sum of $15 then also return true.
                    # and decrease the count of fives by 3 since we would need 3 notes.
                    count_fives -= 3
                else:
                     # If we don't have enough change to give back then return False.
                    return False
        return True
            
                
                    
        