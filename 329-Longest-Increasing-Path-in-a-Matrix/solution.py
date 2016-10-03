class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def DP(i, j):
            if cache[i][j]:
                return cache[i][j]
            
            tmp = 0
            for dir in [(1,0),(-1,0),(0,1),(0,-1)]:
                newI = i + dir[0]
                newJ = j + dir[1]
                if isValid(newI, newJ) and matrix[newI][newJ] > matrix[i][j]:
                    tmp = max(tmp, DP(newI, newJ))
            tmp += 1
            cache[i][j] = tmp
            return tmp
        
        def isValid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False
    
    
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        cache = [[0] * n for i in range(m)]
        maxLen = 0
        for i in range(m):
            for j in range(n):
                maxLen = max(DP(i, j), maxLen)
        return maxLen