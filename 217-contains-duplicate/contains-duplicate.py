class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # HashMap way
        # seen = {}
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen[num] = 1
        # return False
        return len(nums) != len(set(nums))
        