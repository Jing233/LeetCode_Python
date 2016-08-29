# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None:
            return
        nextLevelNode = root

        while nextLevelNode:
            curNode = nextLevelNode
            nextLevelNode, preNode = None, None
            if curNode.left and curNode.right:
                nextLevelNode = curNode.left
                curNode.left.next = curNode.right
                preNode = curNode.right
            elif curNode.left:
                nextLevelNode = curNode.left
                preNode = curNode.left
            elif curNode.right:
                nextLevelNode = curNode.right
                preNode = curNode.right
            
            # decide next level starting point
            while curNode.next:
                curNode = curNode.next
                if curNode.left and curNode.right:
                    if preNode:
                        preNode.next = curNode.left
                    curNode.left.next = curNode.right
                    preNode = curNode.right

                    if not nextLevelNode:
                        nextLevelNode = curNode.left
                elif curNode.left:
                    if preNode:
                        preNode.next = curNode.left
                    preNode = curNode.left
                    if not nextLevelNode:
                        nextLevelNode = curNode.left
                elif curNode.right:
                    if preNode:
                        preNode.next = curNode.right
                    preNode = curNode.right
                    if not nextLevelNode:
                        nextLevelNode = curNode.right
                        
                    
                    

        

            
                
            