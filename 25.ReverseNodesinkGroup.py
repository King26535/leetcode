# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        counter = 0
        while curr != None and counter < k:
            curr = curr.next
            counter += 1
        if counter == k:
            curr = self.reverseKGroup(curr,k)
            while counter > 0:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                counter -= 1
            head = curr
        return head
