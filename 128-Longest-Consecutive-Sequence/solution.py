class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashTable = {}
        for num in nums:
            hashTable[num] = True
        
        maxLen = 0
        while hashTable:
            key = hashTable.popitem()[0]
            left = key
            right = key
            while hashTable and left - 1 in hashTable:
                left -= 1
                del hashTable[left]
            while hashTable and right + 1 in hashTable:
                right += 1
                del hashTable[right]
                
            maxLen = max(right - left + 1, maxLen)
        
        return maxLen
            