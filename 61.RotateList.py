# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        '''
        #version 1.0
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p,q = dummy,dummy
        l = 0
        while p.next:
            p = p.next
            l += 1
        for i in range(l-k%l):
            q = q.next
        p.next = dummy.next
        dummy.next = q.next
        q.next = None
        return dummy.next
        '''
        #version 2.0
        if head == None or head.next == None:
            return head
        newH,tail = head,head
        l = 1
        while tail.next:
            l += 1
            tail = tail.next
        tail.next = head
        for i in range(l-k%l):
            tail = tail.next
        newH = tail.next
        tail.next = None
        return newH
