class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # The next greater list to be returned
        next_greater_list = []

        # For each element in findNums array
        # iterate through entire nums array
        for findNum in findNums:
            next_greater = -1
            has_element = False
            for num in nums:
                # Find the element findNum in nums array
                if findNum == num:
                    has_element = True
                # Once the findNum element is found in nums array
                # henceforth, look up for the next bigger element
                if has_element and num > findNum:
                    next_greater = num
                    break
            next_greater_list.append(next_greater)

        return next_greater_list
