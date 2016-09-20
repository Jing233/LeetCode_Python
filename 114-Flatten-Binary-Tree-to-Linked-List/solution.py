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
        
        def preOrder(node, nodes):
            if node is None:
                return 
            nodes.append(node)
            preOrder(node.left, nodes)
            preOrder(node.right, nodes)
        
        
        nodes = []
        preOrder(root, nodes)
        right = None
        while nodes:
            node = nodes.pop()
            node.right = right
            node.left = None
            right = node
        
        #return root
        
                

            
        