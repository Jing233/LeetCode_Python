class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def computeFreq(word):
            freqList = [0 for _ in range(26)]
            for ch in word:
                freqList[ord(ch) - ord('a')] += 1
            return tuple(freqList)
        
        hashTable = {}
        for word in strs:
            key = computeFreq(word)
            if key in hashTable:
                hashTable[key].append(word)
            else:
                hashTable[key] = [word]
        
        return hashTable.values()
        