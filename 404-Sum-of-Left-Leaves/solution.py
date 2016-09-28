# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inOrder(root, res):
            if root.left:
                if not (root.left.left or root.left.right):
                    res.append(root.left.val)
                inOrder(root.left, res)
            if root.right:
                inOrder(root.right, res)
            
        res = []
        if root:
            inOrder(root, res)
        return sum(res)