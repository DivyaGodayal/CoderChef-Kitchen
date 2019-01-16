class Solution(object):
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """ 
        result = []
        # We will start with an empty string which is our root node located at 0th level
        self.helper("",result,0,n)
        return result
        
    
    def helper(self,expression,result,level,n):
        
        # This is the recursive condition
        # If we are at leaf node till then we will check whether the string is a valid expression or not
        # If its valid we add it to our result or we will discard it  
        if level==n*2:
            if self.checker(expression):
                result.append(expression)
            return
        
        
        # We will call this function in a recursive manner by adding both the
        # opening and closing bracket to the current expression which will check 
        # the current path is a valid path from root to leaf node.
        self.helper(expression+"(",result,level+1,n)
        self.helper(expression+")",result,level+1,n)
        
    
    
    # This function checks the validity of the expression
    def checker(self,expression):
        stack=[]
        for ch in expression:
            if ch=="(":
                stack.append(ch)
            elif ch==")":
                if not stack:
                    return False
                elif stack[-1]=="(":
                    stack.pop()
                else:
                    return False
        return len(stack)==0



