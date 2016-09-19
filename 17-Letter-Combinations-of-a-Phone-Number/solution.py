class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def recur(digits, mapping, path, res):
            if digits == '':
                res.append(path)
                return
            for letter in mapping[digits[0]]:
                recur(digits[1:], mapping, path + letter, res)
        
        mapping = {'0' : ' ',
                   '1' : '',
                   '2' : 'abc',
                   '3' : 'def',
                   '4' : 'ghi',
                   '5' : 'jkl',
                   '6' : 'mno',
                   '7' : 'pqrs',
                   '8' : 'tuv',
                   '9' : 'wxyz'}
        res = []
        if digits:
            recur(digits, mapping, '', res)
        return res