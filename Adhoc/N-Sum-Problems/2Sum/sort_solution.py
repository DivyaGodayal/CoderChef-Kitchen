class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        N = len(nums)
        nums = [(n, i) for i, n in enumerate(nums)]
        nums.sort()

        left, right = 0, N - 1
        while left < right:
            a, b = nums[left][0], nums[right][0]
            if a + b < target:
                left += 1
            elif a + b > target:
                right -= 1
            else:
                return [nums[left][1], nums[right][1]]
