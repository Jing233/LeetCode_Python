class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, start, path, tempSum, target, res):
            if tempSum > target:
                return
            elif tempSum == target:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                dfs(candidates, i, path + [candidates[i]], tempSum + candidates[i], target, res)
        
        res = []
        dfs(candidates, 0, [], 0, target, res)
        return res