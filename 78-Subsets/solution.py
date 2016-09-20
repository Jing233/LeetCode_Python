class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recur(nums, start, path, res):
            if nums is []:
                return 
            res.append(path)
            for i in range(start, len(nums)):
                recur(nums, i + 1, path + [nums[i]], res)
        
        res = []
        recur(nums, 0, [], res)
        return res
        
        