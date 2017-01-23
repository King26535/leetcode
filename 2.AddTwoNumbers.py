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
        result = self.reverse(l1)+self.reverse(l2)
        return self.inreverse(result)
        
    def reverse(self, a):
        if a.next is None:
            return a.val
        else:
            return a.val + 10*self.reverse(a.next)
            
    def inreverse(self, a):
        if a/10 != 0:
            result = ListNode(a%10)
            result.next = self.inreverse(a/10)
            return result
        else:
            return ListNode(a)
