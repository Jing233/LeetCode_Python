class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        import string
        import collections
        def buildPath(path, word):
            if len(preMap[word]) == 0:
                result.append([word] + path[::-1])
                return
            
            path.append(word)
            for w in preMap[word]:
                buildPath(path, w)
            path.pop()
        
        
        wordlist.add(beginWord)
        wordlist.add(endWord)
        
        length = len(beginWord)
        preMap = collections.defaultdict(list)

        result = []
        curLevel = {beginWord}
        while True:
            preLevel = curLevel
            curLevel = set()
            for word in preLevel:
                wordlist.remove(word)
            for word in preLevel:
                for i in range(length):
                    left = word[:i]
                    right = word[i +1:]
                    for c in string.lowercase:
                        if c != word[i]:
                            nextWord = left + c + right
                            if nextWord in wordlist:
                                preMap[nextWord].append(word)
                                curLevel.add(nextWord)
            
            if not curLevel:
                return []
            if endWord in curLevel:
                break
        
        buildPath([], endWord)
        return result