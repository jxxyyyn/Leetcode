class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagram_groups = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
        
            if sorted_str not in anagram_groups:
                anagram_groups[sorted_str] = [s]
            else:
                anagram_groups[sorted_str].append(s)
                
        return list(anagram_groups.values())