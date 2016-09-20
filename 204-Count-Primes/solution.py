class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        
        if n <= 1:
            return 0
            
        primeTable = [True for i in xrange(n)]
        primeTable[0], primeTable[1] = False, False
        counter = 0
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if primeTable[i]:
                counter += 1
                temp = i * i
                while temp < n:
                    primeTable[temp] = False
                    temp += i
        counter = 0
        for prime in primeTable:
            if prime:
                counter += 1
        return counter