class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[j] = num
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1
        
        
        
        