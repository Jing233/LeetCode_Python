# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        import sys
        
        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy
            while l1 or l2:
                val1 = l1.val if l1 else sys.maxint
                val2 = l2.val if l2 else sys.maxint
                if val1 >= val2:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 = l1.next
                cur = cur.next
            return dummy.next
            
        
        pqueue = []
        for node in lists:
            if node is None:
                continue
            heapq.heappush(pqueue, (node.val, node))
        size = len(pqueue)
        for _ in xrange(size - 1):
            _, head1 = heapq.heappop(pqueue)
            _, head2 = heapq.heappop(pqueue)
            head3 = merge(head1, head2)
            heapq.heappush(pqueue, (head3.val, head3))
        if size == 0:
            return None
        return pqueue[0][1]
            