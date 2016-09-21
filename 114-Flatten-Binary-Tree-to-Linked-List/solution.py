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
        rightStack = []
        
        cur = root
        while cur:
            if cur.left:
                if cur.right:
                    rightStack.append(cur.right)
                cur.right = cur.left
                cur.left = None
            else:
                if not cur.right and rightStack:
                    temp = rightStack.pop()
                    cur.right = temp
            cur = cur.right
            
        