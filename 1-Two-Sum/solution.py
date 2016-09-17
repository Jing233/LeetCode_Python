class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hashTable:
                return [hashTable[temp], i] 
            hashTable[nums[i]] = i
        
            
        