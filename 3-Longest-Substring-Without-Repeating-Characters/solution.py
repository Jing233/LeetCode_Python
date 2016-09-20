class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashTable = {}
        left = 0
        maxLen = 0
        resLeft = 0
        resRight = 0
        for right in range(len(s)):
            hashTable[s[right]] = hashTable.get(s[right], 0) + 1
            while hashTable[s[right]] > 1:
                hashTable[s[left]] -= 1
                left += 1
            if right - left > maxLen:
                maxLen = right - left
                resLeft = left
                resRight = right
                
        return len(s[resLeft : resRight + 1])
        