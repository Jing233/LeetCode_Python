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
        def inOrder(root):
            left = right = 0
            if root.left:
                if not (root.left.left or root.left.right):
                    left += root.left.val
                left += inOrder(root.left)
            if root.right:
                right += inOrder(root.right)
            return left + right
            
        return inOrder(root) if root else 0
        