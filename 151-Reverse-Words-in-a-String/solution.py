class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = reversed(s.strip().split())
        
        
        return ' '.join(res)