class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hashTable = {}
        right = 0
        left = 0
        maxLen = 0
        while right < len(s):
            if s[right] in hashTable:
                while left < right and s[right] in hashTable:
                    del hashTable[s[left]]
                    left += 1
            hashTable[s[right]] = True
            right += 1
            maxLen = max(maxLen, right - left)
        print maxLen
        return maxLen