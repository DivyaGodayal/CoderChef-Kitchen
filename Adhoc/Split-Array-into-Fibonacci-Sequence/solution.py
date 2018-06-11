class Solution(object):
    def checkFib(self, start, first, second, S):
        ans = [first, second]
        while start < len(S):
            # Next element in the fibonacci sequence
            third = first + second
            l = len(str(third))
            # We check if this new element exists in the original sequence and if it has any trailing zeros or not
            if third > (2**31 - 1) or long(S[start : start + l]) != third or (S[start] == '0' and third > 0):
                return False, []
            
            first = second
            second = third
            start = start + l
            ans.append(third)
        # If this fibonacci sequence had more than 3 elements, we got ourselves an answer.    
        return len(ans) >= 3 , ans    
    
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        length = len(S)
        """ 
            Each entry of the fibonacci sequence has to be < 2^31 - 1 according to the 
            question. So, we can only consider 11 digits at max (see the value of 2^31).
        """
        for i in range(11):
            for j in range(i+1, i+11):
                
                # first and second entries of the fibonacci sequence. 
                first = S[0 : i + 1]
                second = S[i + 1 : j]
                
                # The number of digits might be < 11, so these additional checks
                if first:
                    first_L = long(first)
                if second:
                    second_L = long(second)
                
                """ 
                    With 11 digits also, we can have a number larger than 2^31 - 1 and hence this check
                    Also, according to the question, we don't have to consider leading zeros, so 
                    the length check. 
                """
                if first <= (2**31 - 1) and second <= (2**31 - 1) and len(str(first)) == (i + 1) and len(str(second)) == (j - i - 1):
                    boolean, result = self.checkFib(j, first, second, S)
                    if boolean:
                        return result
        return []            
                        
            
                
                    
