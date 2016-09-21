class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        import string
        def bfs(wordList, toVisit, depth):
            if len(toVisit) == 0:
                return 0
            tempToVisit = []
            for word in toVisit:
                for i in range(len(word)):
                    for replace in string.lowercase:
                        tempWord = word[:i] + replace + word[i + 1:]
                        if tempWord == endWord:
                            return depth + 1
                        if tempWord in wordList:
                            wordList.remove(tempWord)
                            tempToVisit.append(tempWord)
            
            return bfs(wordList, tempToVisit, depth + 1)
            
        toVisit = [beginWord]
        if beginWord == endWord:
            return 1
        wordList.discard(beginWord)
        return bfs(wordList, toVisit, 1)