class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        hashTable = {}
        for ch in s:
            hashTable[ch] = hashTable.get(ch, 0) + 1
        for ch in t:
            if ch in hashTable:
                if hashTable[ch] == 1:
                    del hashTable[ch]
                else:
                    hashTable[ch] -= 1
            else:
                return False
        
        if len(hashTable):
            return False
        else:
            return True
        