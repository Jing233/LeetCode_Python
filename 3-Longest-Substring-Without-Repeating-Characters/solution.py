class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        
        hashTable = collections.defaultdict(int)
        left = right = maxLen = 0
        while right < len(s):
            hashTable[s[right]] += 1
            while hashTable[s[right]] > 1:
                hashTable[s[left]] -= 1
                left += 1
            right += 1
            maxLen = max(maxLen, right - left)
        return maxLen