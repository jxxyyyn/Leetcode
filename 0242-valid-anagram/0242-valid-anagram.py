class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        list_s = []
        list_t = []
        
        if len(s) != len(t):
            return False
        
        if sorted(s) == sorted(t):
            return True
        return False