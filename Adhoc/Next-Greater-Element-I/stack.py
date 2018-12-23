from collections import Counter
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # dictionary to (element, next greater element) mapping
        find_nums_dict = {}

        # index pointer starting from the right
        right = len(nums) - 1
        # stack to keep track of all the greater elements to right of an element.
        stack = [-1]

        # Starting the last index iterate the nums array
        while right >= 0:
            # For every element, compare with the stack top and keeping popping
            # stacks top element till the stack top has a lesser element than the current element.
            # This is because the current value is a higher value. If we look from the left of this
            # We already have a higher number, so all the smaller numbers at the stack top could be removed.
            while stack and nums[right] > stack[-1]:
                stack.pop()
            # After removing all the smaller elements,
            # the current top if one exits would be the next bigger element for the current element.
            find_nums_dict[nums[right]] = stack[-1] if stack else -1
            stack.append(nums[right])
            right -= 1

        ans = []
        # Now that we have a dictionary of all the next greater elements for each number,
        # We can use that to form an array of next big number for findNums array.
        for findNum in findNums:
            ans.append(find_nums_dict[findNum])

        return ans


            
