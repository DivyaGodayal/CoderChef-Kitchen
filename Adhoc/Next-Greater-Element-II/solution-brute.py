class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # The next greater list to be returned
        next_greater_list = []

        # Since circular search is allowed, we double up the array.
        doubledNums = nums + nums

        # For each element in nums array
        # Start from the next index onwards
        # and look for the next greater in the doubled up nums array.
        for i, findNum in enumerate(nums):
            next_greater = -1
            for num in doubledNums[i+1:]:
                # Look up for the next bigger element
                if num > findNum:
                    next_greater = num
                    break
            next_greater_list.append(next_greater)

        return next_greater_list
