class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import sys
        
        minPrice = sys.maxint
        maxGain = 0
        
        for price in prices:
            if price < minPrice:
                minPrice = price
            maxGain = max(maxGain, price - minPrice)
        return maxGain
        