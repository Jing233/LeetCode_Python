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
        

        def postOrder(root, prev):
            if root is None:
                return prev
            
            prev = postOrder(root.right, prev)
            prev = postOrder(root.left, prev)
            
            root.right = prev
            root.left = None
            prev = root
            return prev
        
        prev = None
        postOrder(root, prev)
        #return root
        
                

            
        