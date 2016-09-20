class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        start = 0
        sign = 1
        if str[0] == '+':
            start += 1
        elif str[0] == '-':
            start += 1
            sign = -1
        val = 0
        for i in range(start, len(str)):
            if str[i] in '0123456789':
                val = 10 * val + ord(str[i]) - ord('0')
            else:
                break
        
        val *= sign
        if val > 2**31 - 1:
            return 2**31 - 1
        elif val <= -2**31:
            return -2**31
        return val 
            