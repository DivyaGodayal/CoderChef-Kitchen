class Solution:
    def twoSum(self, nums, target, left, right):
        pair = []
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                pair.append((nums[left], nums[right]))
                left += 1
                right -= 1
        return pair


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        ans = []
        done = {}
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                a, b = nums[i], nums[j]
                twoSumPairs = self.twoSum(nums, target - a - b, j + 1, N - 1)
                for c, d in twoSumPairs:
                    if (a, b, c, d) not in done:
                        ans.append((a, b, c, d))
                        done[(a, b, c, d)] = 1
        return ans            
