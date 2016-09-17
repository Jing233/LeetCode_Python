class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexOrder = sorted(range(len(nums)), key=lambda i: nums[i])
        
        left = 0
        right = len(nums) - 1
        while left < right:
            temp = nums[indexOrder[left]] + nums[indexOrder[right]]
            if temp > target:
                right -= 1
            elif temp < target:
                left += 1
            else:
                return [indexOrder[left], indexOrder[right]]
        