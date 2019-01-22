class Solution(object):
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = []
        left,right = n,n
        self.helper("",result,left,right)
        return result
        
    
    def helper(self,paranthesis,result,left,right):
        
        if right<left:
            return
        
        if left==0 and right==0:
            result.append(paranthesis)
        
        if left:
            self.helper(paranthesis+"(",result,left-1,right)
        if right:
            self.helper(paranthesis+")",result,left,right-1)
        
