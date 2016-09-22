class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        xPositions = []
        yPositions = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    xPositions.append(i)
                    yPositions.append(j)
                    
        
        #xPositions = sorted(xPositions)
        yPositions = sorted(yPositions)
        minDistance = 0
        left = 0
        right = len(xPositions) - 1
        while left < right:
            minDistance += xPositions[right] - xPositions[left] + yPositions[right] - yPositions[left]
            left += 1
            right -= 1
        return minDistance