class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        k=k%length
        #reverse entire array
        self.reverse(nums, 0, length-1)
        #reverse subarrays
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length-1)
           
    def reverse(self, nums, start, end):
        while(start<end):
            nums[start], nums[end]=nums[end], nums[start]
            start=start+1
            end=end-1
            
