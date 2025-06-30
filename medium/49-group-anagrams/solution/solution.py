class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words= {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in words:
                words[key] = []
            words[key].append(word)
        
        return words.values()

         