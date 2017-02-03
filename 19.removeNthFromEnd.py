class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0) #to delete the first node
        dummy.next = head
        p1 = p2 = dummy
        for i in xrange(n):
            p1 = p1.next
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
