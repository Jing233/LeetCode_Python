class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0        # start of 1s, color white
        right = len(nums) - 1    # position of the last element has not been seen
        
        i = 0
        while i <= right:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            
        
        
        