class Solution(object):
    def __init__(self):
        self.memo = {}
        
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        if N in self.memo:
            return self.memo[N]
        
        # For inputs N = 1 to N = 6, the maximum is N itself.      
        if N <= 6:
            self.memo[N] = N
            return N
        
        ans = 0
        
        # To try all combinations from N-3 down to 1
        # Breaking into sub-problems
        # F(N) = MAX(F(j) * (N - j -1)) where N-3 <= j <= 1 
        for i in range(N-3, 0, -1):
            ans = max(ans, self.maxA(i) * (N-i-1))
        self.memo[N] = ans
        return ans
        
