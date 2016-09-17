# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            sum = l1.val + l2.val + carry
            cur.next = ListNode(sum % 10)
            carry = sum / 10
            cur, l1, l2 = cur.next, l1.next, l2.next
        
        if l1:
            l3 = l1
        else:
            l3 = l2
        while l3:
            sum = l3.val + carry
            cur.next = ListNode(sum % 10)
            carry = sum / 10
            cur, l3 = cur.next, l3.next
        
        if carry:
            cur.next = ListNode(1)
        return dummy.next