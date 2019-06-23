class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                summation = sum(nums[i:j+1])
                if k==0:
                    if summation==0:
                        return True
                elif summation%k==0:
                    return True
        return False