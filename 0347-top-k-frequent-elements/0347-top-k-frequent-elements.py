class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        from collections import Counter
        counted_nums = Counter(nums)
        counted_nums = counted_nums.most_common(k)
        
        frequentElements = []
        for i in counted_nums:
            frequentElements.append(i[0])
            
        return frequentElements
