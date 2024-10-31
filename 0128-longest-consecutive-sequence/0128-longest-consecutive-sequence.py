class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_set= set(nums)
        longest = 0
        
        if len(nums_set) == 1:
            return 1
        
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num
                current_streak = 1
            
                while current_num+1 in nums_set:
                    current_num += 1
                    current_streak +=1
                longest = max(longest, current_streak)
        
        return longest