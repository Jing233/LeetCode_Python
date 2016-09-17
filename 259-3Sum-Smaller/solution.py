class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res