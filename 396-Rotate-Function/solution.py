class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A == []:
            return 0
        sumA = sum(A)
        lastF = 0
        for i, num in enumerate(A):
            lastF += i * num
        maxF = lastF
        i = 0
        while i < len(A):
            F = lastF - sumA + len(A) * A[i] 
            maxF = max(F, maxF)
            lastF = F
            i += 1
        return maxF