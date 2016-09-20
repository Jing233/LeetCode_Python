# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        hashTable = {}   # key, old Node : val, new Node
        cur = head
        while cur:
            hashTable[cur] = RandomListNode(cur.label)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                hashTable[cur].next   = hashTable[cur.next]
            if cur.random:
                hashTable[cur].random = hashTable[cur.random]
            cur = cur.next
        
        if head:
            return hashTable[head]
        else:
            return head