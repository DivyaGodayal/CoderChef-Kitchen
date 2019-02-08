class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        a, b, result = 1, 1, 1
        for i in range(2, n + 1):
            result = a + b
            a, b = b, result
        return result

        
