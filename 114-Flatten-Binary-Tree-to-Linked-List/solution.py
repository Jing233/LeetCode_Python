# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def recur(root):
            if root is None:
                return None
            left = recur(root.left)
            right = recur(root.right)
            if left:
                root.left = None
                root.right = left
                while left.right:
                    left = left.right
                left.right = right
            return root
        recur(root)

            
        