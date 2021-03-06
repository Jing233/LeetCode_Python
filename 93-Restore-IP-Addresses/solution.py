class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValidPart(part):
            if len(part) == 3:
                return 100 <= int(part) <= 255
            elif len(part) == 2:
                return part[0] != '0'
            else:
                return True
        
        def dfs(s, path, res):
            if s == '' and len(path) == 4:
                res.append('.'.join(path))
                return
            if len(path) > 4:
                return
            for i in range(1, min(4, len(s)+1)):
                if isValidPart(s[:i]):
                    dfs(s[i:], path + [s[:i]], res)
        
        res = []
        if len(s) > 12 or len(s) < 4:
            return res
        dfs(s, [], res)
        return res
                