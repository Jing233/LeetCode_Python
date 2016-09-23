class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ''
        while i >=0 or j >= 0:
            val1 = int(a[i]) if i >= 0 else 0
            val2 = int(b[j]) if j >= 0 else 0
            val = (val1 + val2 + carry) % 2
            carry = (val1 + val2 + carry) / 2
            res += str(val)
            i -= 1
            j -= 1
        
        if carry:
            res += '1'
        return res[::-1]