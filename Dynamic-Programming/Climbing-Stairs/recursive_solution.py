class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        memo = {}
        def findAll(n : 'int'):
            # Base case
            if n == 0:
                return 1

            # If we have the cached result, return
            if n in memo:
                return memo[n]

            # This will always be called
            ans = findAll(n - 1)

            # Only call this if n > 2
            if n >= 2:
                ans += findAll(n - 2)

            # cache the results for future use    
            memo[n] = ans
            return ans
        return findAll(n)
