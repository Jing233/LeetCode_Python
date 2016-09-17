class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        i = 0
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                temp = nums[left] + nums[right]
                if temp > target:
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res
        