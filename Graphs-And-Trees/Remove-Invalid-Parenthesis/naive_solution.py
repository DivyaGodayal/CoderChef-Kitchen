from copy import deepcopy
answers = None
min_ignored = None

class Solution(object):
    """
        string: The original string we are recursing on.
        index: current index in the original string. 
        left: number of left parenthesis till now.
        right: number of right parenthesis till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parenthesis ignored in this particular recursion.
    """
    def remaining(self, string, index, left, right, ans, ignored):
        global answers, min_ignored
        
        # If we have reached the end of string. 
        if index == len(string):
            if left == right:
                # This is the resulting expression. Strings are immutable so we move around a 
                # list in the recursion and eventually join to get the final string. 
                possible_ans = "".join(ans)
                
                # If the number of ignored paranthesis in this recursion are equal to the current minimum, record
                # the current expression by adding it to our set. 
                # Since it's a set, duplicates would be handled accordingly
                if ignored == min_ignored:
                    answers.add(possible_ans)
                elif ignored < min_ignored:
                    # If the number of ignored parenthesis in this recursion are better than 
                    # the current minimum, ignore all previous answers, update the minimum and 
                    # record this expression.
                    min_ignored = ignored
                    answers = set([possible_ans])
            return
        
        # If the current character is not a parenthesis, just recurse one step ahead.
        if string[index] not in ['(', ')']:
            ans.append(string[index])
            self.remaining(string, index + 1, left, right, ans, ignored)
            ans.pop()
        else:
            # Else, one recursion is with ignoring the current character. So, we increment the ignored
            # counter and leave the left and right untouched. 
            self.remaining(string, index + 1, left, right, ans, ignored + 1)
            
            # If the current parenthesis is an opening bracket, we consider it and increment left and 
            # move forward
            if string[index] == '(':
                ans.append('(')
                self.remaining(string, index + 1, left + 1, right, ans, ignored)
                ans.pop()
            elif right < left:
                # If the current parenthesis is a closing bracket, we consider it 
                # only if we have more number of opening brackets that can possibly match it, and 
                # increment right and move forward.
                ans.append(")")
                self.remaining(string, index + 1, left, right + 1, ans, ignored)
                ans.pop()
    
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        # Reset the global variables that we use for every test case. 
        global answers, min_ignored
        answers = set()
        
        # That's the upper bound on the characters that can be removed at max. 
        min_ignored = len(s)
        
        # Recursive call
        self.remaining(s, 0, 0, 0, [], 0)
        return list(answers)
        
