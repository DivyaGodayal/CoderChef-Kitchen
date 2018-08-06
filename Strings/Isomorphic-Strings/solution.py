class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Dictionaries to store the letter position.
        # We can assign a unique number to every unqiue character we encounter in an incremental order.      
        s_dict = {}
        t_dict = {}
        # counters to keep track of the number of unique characters in each string.   
        digit_s = 0
        digit_t = 0
        # traverse both the strings parallely and pick a character one by one.
        for ch_s,ch_t in zip(s,t):
            if ch_s not in s_dict:
                # if the character encountered is not in the corresponding dictionary 
                # then assign the next unique counter value to the character
                s_dict[ch_s] = digit_s + 1
                digit_s += 1
            
            if ch_t not in t_dict:
                # if the character encountered is not in the corresponding dictionary 
                # then assign the next unique counter value to the character 
                t_dict[ch_t] = digit_t + 1
                digit_t += 1
            
            # if the numberic counter parts for character in s and t are not same at any point
            # this means the strings are not isomorphic.
            if s_dict[ch_s] != t_dict[ch_t]:
                return False
        return True
                
            
        
