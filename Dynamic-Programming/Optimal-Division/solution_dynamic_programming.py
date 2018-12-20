class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        memo = {}
        parent = {}

        # Function to calculate the maximum
        # expression value that we can achieve from the given set of numbers.
        def recurse(start, end):

            # base case
            if start == end:
                return nums[start], nums[start]

            ans = float("-inf")
            for i in range(start, end):

                # Try all possible split points
                left_max, left_min = recurse(start, i)
                right_max, right_min = recurse(i + 1, end)

                # N_Max / D_Min
                result = left_max / right_min

                # Record the best answer for memoization + backtracking
                if result > ans:
                    ans = result
                    parent[(start, end)] = i
            memo[(start, end)] = ans
            return left_max / right_min, left_min / right_max

        # Function to backtrack and form the actual expression
        def backtrace(start, end, is_max):
            if start == end:
                return str(nums[start])

            i = parent[(start, end)]

            # Maximize the numerator and minimize the denominator.
            left_str = backtrace(start, i, True)
            right_str = backtrace(i + 1, end, False)

            # More than 1 element
            if i + 1 < end and is_max:
                return "{}/({})".format(left_str, right_str)
            return "{}/{}".format(left_str, right_str)

        recurse(0, len(nums) - 1)
        return backtrace(0, len(nums) - 1, True)
