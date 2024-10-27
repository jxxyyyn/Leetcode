class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq

        counted_nums = Counter(nums)
        return [num for num, _ in heapq.nlargest(k, counted_nums.items(), key=lambda x: x[1])]