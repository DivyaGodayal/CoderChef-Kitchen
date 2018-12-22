class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """

        N = len(A)
        memo = {}

        # Maintaining the cumulative sum for optimization
        cumulative_sum = [0]
        val = 0
        for a in A:
            val += a
            cumulative_sum.append(val)

        def recurse(index, groups_formed):
            if index == N:
                return 0

            # The optimization comes in very handy here. This is a O(1) operation
            if groups_formed == K - 1:
                return (cumulative_sum[-1] - cumulative_sum[index]) / (N - index)

            # Return cached result
            if (index, groups_formed) in memo:
                return memo[(index, groups_formed)]

            s = 0
            ans = float("-inf")
            # Try all split indices for "split index"
            for i in range(index, N):
                s += A[i]
                ans = max(ans, s / (i - index + 1) + recurse(i + 1, groups_formed + 1))

            # Cache the answer
            memo[(index, groups_formed)] = ans
            return ans
        return recurse(0, 0)
