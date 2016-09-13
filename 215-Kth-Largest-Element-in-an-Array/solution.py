class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # use partitioning in quickSort
        
        def partition(nums, start, end):
            pivot = nums[end]
            left = start
            for i in range(start, end):
                if nums[i] <= pivot:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
            nums[left], nums[end] = nums[end], nums[left]
            return left
            
            
        pos = partition(nums, 0, len(nums) - 1)
        print nums
        while pos != len(nums) - k:
            if pos > len(nums) - k:
                pos = partition(nums, 0, pos - 1)
            else:
                pos = partition(nums, pos + 1, len(nums) - 1)

        return nums[pos]
        