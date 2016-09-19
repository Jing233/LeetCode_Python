class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] and s > 0:
            return 0
            
        left = 0
        right = 0
        minLen = len(nums) + 1
        subArrSum = 0
        while right < len(nums):
            subArrSum += nums[right]
            while left <= right and subArrSum >= s:
                minLen = min(minLen, right - left + 1)
                subArrSum -= nums[left]
                left += 1
            right += 1
        
        if minLen == len(nums) + 1:
            return 0
        return minLen