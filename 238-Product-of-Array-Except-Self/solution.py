class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prodFromHead = [1 for i in nums]
        prodFromTail = [1 for i in nums]
        for i in xrange(1, len(nums)):
            prodFromHead[i] = prodFromHead[i - 1] * nums[i - 1]
        
        res = [1 for i in nums]
        res[-1] = prodFromHead[-1]
        for i in reversed(xrange(len(nums) - 1)):
            prodFromTail[i] = prodFromTail[i + 1] * nums[i + 1]
            res[i] = prodFromTail[i] * prodFromHead[i]
        
        return res
        