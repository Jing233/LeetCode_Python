# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        class ResultType:
            def __init__(self, isBST, minVal=sys.maxint, maxVal=-1-sys.maxint):
                self.isBST  = isBST
                self.minVal = minVal
                self.maxVal = maxVal
        
        
        def recur(node):
            if node is None:
                return ResultType(True)
            left = recur(node.left)
            right = recur(node.right)
        
            if left.isBST and right.isBST and left.maxVal < node.val < right.minVal:
                return ResultType(True, min(left.minVal, node.val), max(right.maxVal, node.val))
            else:
                return ResultType(False)
        
        return recur(root).isBST
        