class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The list to store next greater elements
        ans = [-1] * len(nums)

        # Stack to keep track of all the greater elements to right of an element.
        stack = [-1]

        start = 0
        max_ = float("-inf")

        # Find the maximum element index
        for i in range(len(nums)):
            if nums[i] > max_:
                max_ = nums[i]
                start = i

        # Starting the last index iterate the nums array
        for i in range(len(nums)):
            index = (len(nums) + (start - i)) % len(nums)

            # For every element, compare with the stack top and keeping popping
            # stacks top element while the stack top has a lesser element than the current element.
            while stack and nums[index] >= stack[-1]:
                stack.pop()

            # After removing all the smaller elements,
            # the current top if one exits would be the next bigger element for the current element.
            ans[index] = stack[-1] if stack else -1
            stack.append(nums[index])

        return ans
