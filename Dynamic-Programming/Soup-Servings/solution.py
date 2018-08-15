class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        memo = {}
        # When N is very large, we return 1 always, this can be seen empirically.
        if N > 4800:
            return 1
        # Recursive function which takes soup quantity for A and B
        # and returns probability that soup A will be empty first,
        # and the probability that A and B become empty at the same time
        # the answer is returned in the form of a tuple (T1, T2)
        # Where T1 is the probability that A got empty first
        # and T2 is the probability that A and B will become empty at the same time.
        def recurse_soup(A,B):
            # Memoizing the answer corresponding to a pair of A and B values.
            if (A,B) in memo:
                return memo[(A,B)]
            # Base case for both getting empty , Hence (T1 = 0 , T2 = 1)
            if A <= 0 and B <= 0:
                return (0,1)
            
            # Base case for A getting empty first , Hence (T1 = 1 , T2 = 0)
            if A <= 0 and B > 0:
                return (1, 0)
            
            # If B gets empty first then return (0,0) since this not part of the probability we are aiming for.
            if A > 0 and B <= 0:
                return (0, 0)
            
            # Recurse for all the operations which the question demands.
            X = recurse_soup(A-100,B)
            Y = recurse_soup(A-75,B-25)
            Z = recurse_soup(A-50,B-50)
            W = recurse_soup(A-25,B-75)
            
            # Adding all the returned tuple values respectively, and multiplying by 0.25.
            # Since every operation has a probability of 0.25, hence we multiply by 0.25.
            ans = (0.25 * (X[0] + Y[0] + Z[0] + W[0]) , (0.25 * (X[1] + Y[1] + Z[1] + W[1])))
            memo[(A,B)] = ans
            return ans
        
        # The answer we return is the sum of (T1, T2) and T2 is divided by 2.
        a = recurse_soup(N,N)
        return a[0] + a[1]/2.0
        