class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        import string
        def bfs(wordList, toVisit):
            depth = 1
            while toVisit:
                tempToVisit = []
                for word in toVisit:
                    for i in range(len(word)):
                        for c in string.lowercase:
                            nextWord = word[:i] + c + word[i + 1:]
                            if nextWord == endWord:
                                return depth + 1
                            if nextWord in wordList:
                                wordList.remove(nextWord)
                                tempToVisit.append(nextWord)
                toVisit = tempToVisit
                depth += 1
            return 0
            
        toVisit = [beginWord]
        wordList -= {beginWord, endWord}
        return bfs(wordList, toVisit)