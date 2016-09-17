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
        def inOrder(node, depth, res):
            if node is None:
                return 
            if depth >= len(res):
                res.append(node.val)
            else:
                res[depth] = node.val
            inOrder(node.left, depth + 1, res)
            inOrder(node.right, depth + 1, res)
        res = []
        inOrder(root, 0, res)
        return res