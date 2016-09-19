class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
            
        maxHeight =  0
        maxPos    = -1
        for i, h in enumerate(height):
            if maxHeight < h:
                maxHeight = h
                maxPos    = i
        
        waterTrappedLeft  = 0
        waterTrappedRight = 0
        leftBound = height[0]
        for i in range(maxPos):
            if leftBound < height[i]:
                leftBound = height[i]
            waterTrappedLeft += leftBound - height[i]
        
        rightBound = height[-1]
        for j in reversed(range(maxPos, len(height))):
            if rightBound < height[j]:
                rightBound = height[j]
            waterTrappedRight += rightBound - height[j]
        
        return waterTrappedLeft + waterTrappedRight 