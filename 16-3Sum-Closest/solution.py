class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys
        
        
        nums = sorted(nums)
        diff = sys.maxint
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tripleSum = nums[i] + nums[left] + nums[right]
                #print tripleSum, diff
                if abs(tripleSum - target) < diff:
                    diff = abs(tripleSum - target)
                    res = tripleSum
                    if diff == 0:
                        return target
                elif tripleSum > target:
                    right -= 1
                else:
                    left += 1
        return res
                    
        