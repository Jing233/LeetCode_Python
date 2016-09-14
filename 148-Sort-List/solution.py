# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        def findMidNode(head):

            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
            
        
        def mergeTwoLists(head1, head2):
            dummy = ListNode(0)
            cur = dummy
            while head1 and head2:
                if head1.val < head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next
            
            if head1:
                cur.next = head1
            else:
                cur.next = head2
            
            return dummy.next
            
        def mergeSort(head):
            if not head or not head.next:
                return head
            midNode = findMidNode(head)
            head1 = head
            head2 = midNode.next
            midNode.next = None
            head1 = mergeSort(head1)
            head2 = mergeSort(head2)
            return mergeTwoLists(head1, head2)
        
        return mergeSort(head)
        