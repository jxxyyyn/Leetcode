class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        from collections import Counter
        count_t = Counter(t)
        count_s = Counter(s)
        if count_s == count_t :
            return True
        return False