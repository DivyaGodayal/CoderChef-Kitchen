class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # The cache used to store repeated subproblems
        memo = {}
        
        """
            rem: Tells us the number of 'A's that remain to be printed on the screen.
            buf: The buffer value for paste operations, initially 0.
            
        """
        def recurse(rem, buf):
            # If rem is 0 means all the required 'A's have been printed and no other key needs to be pressed.
            if rem == 0:
                return 0
            
            # If we have this state of the recursion cached, then return it
            if (rem, buf) in memo:
                return memo[(rem, buf)]
            
            # Since we are to minimize the answer, so taking a max value as the initial value
            ans = float("inf")
            
            # Copy all and Paste operation. We had (n - rem) printed on screen. After copy paste it would be 2*(n - rem) and 
            # new remaining would be n - 2*(n - rem)
            new_rem = n - 2*(n - rem)
            
            # If new remaining is >= 0 i.e. if that many 'A's were actually left to be printed, then recurse
            if new_rem >= 0:
                ans = recurse(new_rem, n - rem) + 2
            # If the number of 'A's in the buffer are <= the number of 'A's left to be printed on screen i.e. rem., then recurse 
            if buf > 0 and buf <= rem:
                ans = min(ans, recurse(rem - buf, buf) + 1)
                
            # Cache the answer    
            memo[(rem, buf)] = ans
            return ans    
        
        # We recurse starting from n - 1 because 1 'A' is already printed on the screen.
        return recurse(n - 1, 0)
