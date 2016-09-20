# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def recur(root, res, depth):
            if root is None:
                return
            
            if len(res) == depth:
                res.append(root.val)
            recur(root.right, res, depth + 1)
            recur(root.left, res, depth + 1)
        res = []
        recur(root, res, 0)
        return res
        