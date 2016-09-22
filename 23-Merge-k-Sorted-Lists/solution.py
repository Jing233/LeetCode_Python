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
        if len(lists) == 0:
            return lists
            
        def merge(listA, listB):
            dummy = ListNode(0)
            cur = dummy
            while listA and listB:
                if listA.val <= listB.val:
                    cur.next = listA
                    listA = listA.next
                else:
                    cur.next = listB
                    listB = listB.next
                cur = cur.next
            if listA:
                cur.next = listA
            else:
                cur.next = listB
            return dummy.next
        
        while len(lists) > 1:
            if len(lists) & 1:
                for i in range(1, 1 + len(lists) / 2):
                    lists[i] = merge(lists[i], lists[len(lists) / 2 + i])
                lists = lists[:1 + len(lists) / 2]
            else:
                for i in range(len(lists) / 2):
                    lists[i] = merge(lists[i], lists[len(lists) / 2 + i])
                lists = lists[:len(lists) / 2]
        return lists[0]