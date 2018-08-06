class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        left = 0
        right = 0
        
        # First, we find out the number of misplaced left and right parenthesis. 
        for char in s:
            # Simply record the left one. 
            if char == '(':
                left += 1
            elif char == ')':
                # If we don't have a matching left, then this is a misplaced right, record it. 
                right += not (left > 0)
                # Decrement any left parenthesis because we have found a right which CAN be a matching one for a left.
                left -= (left > 0)
        
        result = {}
        def recurse(s, index, l, r, left, right, ans):
            # If we reached the end of the string, just check if the resulting expression is 
            # valid or not and also if we have removed the total number of left and right 
            # parenthesis that we should have removed.
            if index == len(s):
                # If this expression is indeed valid, we record it in a dictionary. We could have 
                # used a set as well. No duplicates required here.
                if l == r and left == 0 and right == 0:
                    if ans not in result:
                        result[ans] = 1
                return
            
            # Recursion for ignoring a parenthesis. Checks if the parenthesis 
            # can be ignored depending on if left > 0 for '(' or right > 0 for ')'
            if (s[index] == '(' and left > 0) or (s[index] == ')' and right > 0):
                recurse(s, index + 1, l, r, left - (s[index] == '('), right - (s[index] == ')'), ans)
            
            # These recursions are when we don't ignore the current character. 
            # If the current parenthesis is a left, increment `l` and recurse ahead. 
            if s[index] == '(':
                recurse(s, index + 1, l + 1, r, left, right, ans + s[index])
            elif s[index] == ')' and l > r:
                # Else if the current character is a right and if we have seen more left than right 
                # till now in our resulting expression, then consider this right and move forward. 
                recurse(s, index + 1, l, r + 1, left, right, ans + s[index])
            elif s[index] not in ['(', ')']:
                recurse(s, index + 1, l, r, left, right, ans + s[index])
        
        # Now, the left and right variables tell us the number of misplaced left and 
        # right parenthesis and that greatly helps pruning the recursion.
        recurse(s, 0, 0, 0, left, right, "")     
        return list(result.keys())
