class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # if lenD == 1 and lenS ==1 and dict[0]==s[0]: return True
        f = [False for i in range(len(s) + 1)]
        f[0] = True
        
        for i in range(1, len(f)):
            for word in wordDict:
                temp = i - len(word)
                if temp >= 0 and f[temp] and s[temp:i] == word:
                    f[i] = True
                    break
        return f[-1]