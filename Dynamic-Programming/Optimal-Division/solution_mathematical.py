class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        # Base cases
        if len(nums) == 1:
            return "{}".format(nums[0])
        elif len(nums) == 2:
            return "{}/{}".format(nums[0], nums[1])
        
        return "{}/(".format(nums[0]) + "/".join(map(str, nums[1:])) + ")"
