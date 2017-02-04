# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p,q = dummy,dummy
        while p.next != None and p.next.next != None:
            first = p.next
            second = p.next.next
            third = p.next.next.next
            q.next = second
            q.next.next = first
            q.next.next.next = third
            p = p.next.next
            q = q.next.next
        return dummy.next
