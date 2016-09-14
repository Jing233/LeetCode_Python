class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        
        # f[i] means all the possible sentences of s
        # f[i] = if s[j:i] in wordDict, f[i] = [temp.append(s[j:i]) for temp in f[j]]
        
        
        d = [False for i in range(len(s) + 1)]
        d[0] = True
        
        for i in range(1, len(d)):
            for word in wordDict:
                temp = i - len(word)
                if temp >= 0 and d[temp] and s[temp:i] == word:
                    d[i] = True
                    break
        if not d[-1]:
            return []
        
        
        
        
        f = [[] for i in range(len(s) + 1)]
        for i in range(len(f)):
            for word in wordDict:
                temp = i - len(word)
                if (temp == 0 or (temp > 0 and f[temp])) and s[temp:i] == word:
                    if f[i]:
                        if temp == 0:
                            f[i] += [[word]]
                        else:
                            f[i] += [tempList + [word] for tempList in f[temp]]
                    else:
                        if temp == 0:
                            f[i] = [[word]]
                        else:
                            f[i] = [tempList + [word] for tempList in f[temp]]
        
        return [' '.join(temp) for temp in f[-1]]