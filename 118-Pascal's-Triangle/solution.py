class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(numRows - 1):
            temp = [1]
            for j in xrange(len(result[-1]) - 1):
                temp.append(result[-1][j] + result[-1][j + 1])
            temp.append(1)
            result.append(temp)
        return result
        