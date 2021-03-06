class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # keypoint 1: ']'
        # keypoint 2: '['
        
        mapping = {'(':')', '[':']', '{':'}'}
        leftStack = []
        for ch in s:
            if ch in '([{':
                leftStack.append(ch)
            else:
                if leftStack == [] or mapping[leftStack.pop()] != ch:    
                    return False
        
        if leftStack == []:                                             
            return True
        else:
            return False
                