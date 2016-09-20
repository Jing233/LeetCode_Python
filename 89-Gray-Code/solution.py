class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        temp = self.grayCode(n - 1)
        base = 1 << (n - 1)
        return temp + [base + i for i in reversed(temp)]