class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        from collections import Counter
        
        counted_nums = Counter(nums).most_common(k)
        return [num for num, _ in counted_nums]