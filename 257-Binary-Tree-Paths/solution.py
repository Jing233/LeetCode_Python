# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def recur(root, path, res):
            if root.left is None and root.right is None:
                res.append(path)
                return
            if root.left:
                recur(root.left, path + '->' + str(root.left.val), res)
            if root.right:
                recur(root.right, path + '->' + str(root.right.val), res)
    
        res = []
        if root:
            recur(root, str(root.val), res)
        return res