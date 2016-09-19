class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i, num in enumerate(nums):
            if i and nums[i - 1] == num:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tempSum = num + nums[left] + nums[right]
                if tempSum > 0:
                    right -= 1
                elif tempSum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
        return res
                