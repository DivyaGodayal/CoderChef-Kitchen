class Solution(object):
    def partitionLabels(self, S):
        
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []
        
        # dictionary to save the last indices of each unique alphabet
        letter_dict = {}
        ans = []
        for index in range(len(S)):
            letter_dict[S[index]] = index
         
        i = 0 
        last_break_point = 0
        cut_point = letter_dict[S[i]]
        # loop through through the string 
        while cut_point < len(S) and i < len(S):
            cut_point = letter_dict[S[i]]
            # loop through the current partition        
            # which starts at i and ends at cut_point
            while i <= cut_point:
                # if there is any element in the parition whose last index is greater than the current cut_point
                # this means that element lies outside of the current parition
                # so we update the current cut_point to the last index of this element
                if letter_dict[S[i]] > cut_point:
                    cut_point = letter_dict[S[i]]
                i += 1
    
            # add the number of elements in the current partition to the answer list
            ans.append(i-last_break_point)
            last_break_point = i
        
        return ans
                
                
            
