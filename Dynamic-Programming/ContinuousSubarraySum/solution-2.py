class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<2:
            return False
            
        dp = [0]*len(nums)
        dp[0]=nums[0]
        
        for i in range(1,len(nums)):
            dp[i]=dp[i-1]+nums[i]
            
            if k==0 and dp[i]==0:
                return True
            elif k and dp[i]%k==0:
                return True
        
        for i in range(0,len(nums)-2):
            for j in range(i+2,len(nums)):
                if dp[j]-dp[i]==0 and k==0:
                    return True 
                elif k and (dp[j]-dp[i])%k==0:
                    return True
        
        return False