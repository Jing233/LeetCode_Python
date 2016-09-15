# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        # first search the position of the node
        
        cur = root
        found = False
        bigger = None
        while cur and not found:
            if cur.val == p.val:
                found = True
            elif cur.val > p.val:
                bigger = cur
                cur = cur.left
            else:
                cur = cur.right
        
        if found:
            if p.right:
                cur = p.right
                while cur.left:
                    cur = cur.left
                return cur
            else:
                return bigger
        