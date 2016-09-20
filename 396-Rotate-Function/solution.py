class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import sys
        def computeF(A):
            f = 0
            for i, num in enumerate(A):
                f += i * num
            return f
        
        if A == []:
            return 0
        sumA = sum(A)
        maxF = computeF(A)
        lastF = maxF
        i = 0
        while i < len(A):
            F = lastF - sumA + len(A) * A[i] 
            maxF = max(F, maxF)
            lastF = F
            i += 1
        return maxF
        