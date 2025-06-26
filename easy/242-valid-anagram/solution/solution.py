class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen_in_s = {}
        seen_in_t = {}

        for letter in s:
            seen_in_s[letter] = seen_in_s.get(letter, 0) + 1
        
        for letter in t:
            seen_in_t[letter] = seen_in_t.get(letter, 0) + 1
        
        return seen_in_s == seen_in_t
        