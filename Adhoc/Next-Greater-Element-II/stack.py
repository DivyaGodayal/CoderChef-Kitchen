class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The list to store next greater elements
        ans = [-1] * len(nums)
        # Index pointer starting from the right
        # We double up the pointers value to go through the array twice,
        # this helps to imitate a circular array
        right = (2 * len(nums) - 1)
        # stack to keep track of all the greater elements to right of an element.
        stack = [-1]

        # Starting the last index iterate the nums array
        while right >= 0:

            # Since we doubled the arrays length, to make it behave as circular array.
            index = right % len(nums)

            # For every element, compare with the stack top and keeping popping
            # stacks top element while the stack top has a lesser element than the current element.
            while stack and nums[index] >= stack[-1]:
                stack.pop()

            # After removing all the smaller elements,
            # the current top if one exits would be the next bigger element for the current element.
            ans[index] = stack[-1] if stack else -1
            stack.append(nums[index])
            right -= 1

        return ans
