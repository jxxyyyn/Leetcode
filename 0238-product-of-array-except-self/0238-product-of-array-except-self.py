class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums_final = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)) :
            nums_final[i] *= left
            left *= nums[i]
            
        right = 1
        for i in range(len(nums)-1, -1, -1):
            nums_final[i] *= right
            right *= nums[i]
        
        return nums_final