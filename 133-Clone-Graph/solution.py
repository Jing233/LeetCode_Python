# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        
        if not node:
            return node
        nodeMap = {}   # key, old node -> val, new node
        # clone all the nodes
        toVisit = [node]
        while toVisit:
            curNode = toVisit.pop()
            if curNode in nodeMap:
                continue
            else:
                nodeMap[curNode] = UndirectedGraphNode(curNode.label)
                toVisit.extend(curNode.neighbors)
        
        # copy all the neighbors
        for oldNode, newNode in nodeMap.items():
            newNode.neighbors = [nodeMap[tempNode] for tempNode in oldNode.neighbors]
        
        return nodeMap[node]
        
        
        