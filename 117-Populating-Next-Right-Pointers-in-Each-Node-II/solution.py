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
        if not root:
            return root
            
        level = [root]
        while level:
            levelLength = len(level)
            preNode = None
            for i in range(levelLength):
                curNode = level.pop(0)
                if preNode:
                    preNode.next = curNode
                if curNode.left:
                    level.append(curNode.left)
                if curNode.right:
                    level.append(curNode.right)
                preNode = curNode
                