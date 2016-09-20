# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def findMid(head):
                    
            if head is None:
                return None
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        
        def reverse(head):
            pre = None
            cur = head
            while cur:
                curNext = cur.next
                cur.next = pre
                pre = cur
                cur = curNext
            return pre

        
        mid = findMid(head)
        head2 = reverse(mid)
        cur1 = head
        cur2 = head2
        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1, cur2 = cur1.next, cur2.next
        return True