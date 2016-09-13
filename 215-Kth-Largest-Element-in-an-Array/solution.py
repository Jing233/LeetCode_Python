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
            

        start = 0
        end = len(nums) - 1
        pos = partition(nums, start, end)
        while pos != len(nums) - k:
            if pos > len(nums) - k:
                end = pos - 1
            else:
                start = pos + 1
            pos = partition(nums, start, end)

        return nums[pos]
        