class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        hashTable = {}
        left = 0
        for right in xrange(len(s)):
            hashTable[s[right]] = hashTable.get(s[right], 0) + 1
            while left <= right and hashTable[s[left]] > 1:
                left += 1
        return left if left < len(s) else -1
            