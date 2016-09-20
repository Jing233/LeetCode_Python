# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        
        if root is None:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            res.append([])
            levelLen = len(queue)
            for i in xrange(levelLen):
                curNode = queue.popleft()
                res[-1].append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
        return res
                
        