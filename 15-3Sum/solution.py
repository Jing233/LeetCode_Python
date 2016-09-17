class Solution(object):
    def threeSum(self, numbers):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(valueList, k, currentPos):
            #print valueList
            if k == 0 and sum(valueList) == 0:
                res.append(valueList)
            elif k > 0 and sum(valueList) <= 0:
                for i in range(currentPos, len(numbers)):
                    if (i > currentPos) and (numbers[i] == numbers[i - 1]):
                        continue
                    dfs(valueList + [numbers[i]], k - 1, i + 1)
        
        res = []
        numbers.sort()
        dfs([], 3, 0)
        return res
        