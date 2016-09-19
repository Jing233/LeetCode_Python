class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        resLeft, resRight = 0, 0
        resMaxLen = 0
        for center in range(2*len(s)):
            if center & 1:
                left = center / 2 - 1
                right = left + 1
            else:
                left = center / 2
                right = left
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1
            if right - left > resMaxLen:
                resMaxLen = right - left
                resLeft = left
                resRight = right
            
        
        return s[resLeft : resRight + 1]
        