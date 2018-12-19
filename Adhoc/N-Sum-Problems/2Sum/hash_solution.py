class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        N = len(nums)
        hash_ = {}

        for i in range(N):
            if target - nums[i] in hash_:
                return [hash_[target - nums[i]], i]
            hash_[nums[i]] = i
