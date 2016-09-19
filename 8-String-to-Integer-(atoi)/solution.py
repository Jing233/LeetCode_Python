class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        sign = 1
        start = 0
        if str[0] == '+':
            start = 1
        elif str[0] == '-':
            start = 1
            sign = -1
            
        val = 0
        for ch in str[start:]:
            if ch in '0123456789':
                val = 10 * val + ord(ch) - ord('0')
            else:
                break
            
        val = sign * val
        if val > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif val < -2 ** 31:
            return -2 ** 31
        else:
            return val
         