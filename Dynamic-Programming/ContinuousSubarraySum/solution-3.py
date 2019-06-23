class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dp = [0]*len(nums)
        result = {}
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = dp[i-1]+nums[i]
        
        if len(nums)<2:
            return False
        
        if k==0:
            for i in range(1,len(nums)):
                if nums[i]==0 and nums[i-1]==0:
                    return True
            return False
        
        for i in range(len(dp)):
            if not i==0 and dp[i]%k==0:
                return True
            else:
                if not (dp[i]%k in result.keys()):
                    result[dp[i]%k]=i
                else:
                    if i-result[dp[i]%k]>1:
                        return True

        return False