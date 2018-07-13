class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        stack = []
        for s in S:
            # If we find an opening bracket, simply push it
            if s == '(':
                stack.append(s)
            else:
                s = 0
                # [TEST-CASE-SAMPLE-1] Else, keep on popping values from the top of the stack until there are 
                # number there i.e. until we find a matching opening bracket.
                while True:
                    val = stack[-1]
                    stack.pop()    
                    if val == '(':
                        break
                    s += val
                # The value we get here should be doubled according to the question. Any value between parenthesis is to
                # be doubled. 
                stack.append(2*s if s > 0 else 1)
        # [TEST-CASE-SAMPLE-2] We can again have multiple values in the stack remaining. So we sum them all         
        return sum(stack)            

