class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        if not temperatures:
            return []
        
        stack = []
        ans = []
        L = len(temperatures)
        
        # Iterate on the sequence in reverse. 
        for i, t in enumerate(reversed(temperatures)):
            
            # Enumerate starts from 0 no matter what, so had to do this to get the actual index
            i = L - i - 1
            
            # Keep popping elements till we have smaller elements in the stack or until the stack becomes empty.
            while stack and t >= temperatures[stack[-1]]:
                stack.pop()
            
            # If stack becomes empty, then this is the largest element of all elements ahead.
            if not stack:    
                ans.append(0)
            else:
                # Else, the stack top gives the next warmer day.
                ans.append(stack[-1] - i)
            stack.append(i)
            
        # Reverse the list and return.     
        return ans[::-1]    
