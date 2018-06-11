from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        ans = True
        groups = 0
        if not len(hand) % W == 0:
            return False
        # Calculate the frequencies of all hands in the list
        dict_num = Counter(hand)
        # Get all the unique hands from the list of keys
        hand = list(dict_num.keys())
        # Sort the keys 
        hand.sort()
        for i in range(len(hand)): 
            # For each hand 
            current = hand[i]
            if dict_num[current] > 0:
                for j in range(1,W):
                    # Check if you have all the consecutive W numbers for the group to be formed.
                    # Also we should check if we have enough number of consecutive numbers so that the group could be formed.
                    if current+j in dict_num and dict_num[current+j] >= dict_num[current]:
                        dict_num[current+j] -= dict_num[current]
                    else:
                        return False
            dict_num[current] = 0
        return ans
            
                
        
        
