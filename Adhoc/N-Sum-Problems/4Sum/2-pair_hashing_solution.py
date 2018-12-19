from collections import defaultdict

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # Forming the pairs dictionary
        # We use a defaultdict in Python for code efficiency
        pairs = defaultdict(set)
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                sum_ = nums[i]+nums[j]
                pairs[sum_].add((i, j))

        result = set()
        for key in pairs:
            # First pair
            value = target - key
            if value in pairs:
                # Second pair found.

                # list1 and list2
                set1 = pairs[key]
                set2 = pairs[value]
                for (i,j) in set1:
                    for (k,l) in set2:
                        # Forming quadruples
                        if i!=k and i!=l and j!=k and j!=l:
                            flist = [nums[i],nums[j],nums[k],nums[l]]
                            # Sort to avoid duplication
                            flist.sort()
                            result.add(tuple(flist))
        return list(result)
