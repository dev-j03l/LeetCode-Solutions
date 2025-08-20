class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        L, R = 0, len(nums)
        
        while L < R:
            if nums[L] == val:
                R -= 1
                nums[L] = nums[R]
            else:
                L += 1
        return R