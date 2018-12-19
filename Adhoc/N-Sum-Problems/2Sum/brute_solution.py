class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]
