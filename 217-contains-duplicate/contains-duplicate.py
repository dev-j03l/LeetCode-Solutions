class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # HashMap way
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1
        return False
        