class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # Sort the array A
        A.sort()
        # Sort the array B as well.
        # Since the shuffled elements in A need to be placed
        # w.r.t the elements of B, we would need indices of
        # elements in B.
        B = [(i,b) for i, b in enumerate(B)]
        B = sorted(B, key = lambda v : v[1])

        # Two index pointers, one for A and the other for B.
        i = 0
        j = 0
        # New shuffled array A to be formed.
        # Since A would have all positive values
        # A negative value denotes no element present
        shuffled_A  = [-1 for k in range(len(A))]

        # Array to hold all the non advantage elements
        remaining = []

        # Iterate the arrays
        # Find all the advantage elements of A
        while i < len(A):
            # Has advantage
            if A[i] > B[j][1]:
                # Place in the shuffled array
                # At the correct spot, corresponding index of B.
                shuffled_A[B[j][0]] = A[i]
                i += 1
                j += 1
            else:
                # If not an advantage element then save for later
                # in the remaining elements list,
                remaining.append(A[i])
                i += 1

        # Fill all the left over empty spaces in the shuffled A array
        # The elements in these empty spots do not count towards the advantage
        # Hence can be placed in any given order.
        r = 0
        for i in range(len(shuffled_A)):
            if shuffled_A[i] == -1:
                shuffled_A[i] = remaining[r]
                r += 1
        return shuffled_A
