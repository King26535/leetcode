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
        '''#version 1.0 TLE
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        res = lists[0]
        for i in range(len(lists)-1):
            res = self.mergeTwoLists(res, lists[i+1])
        return res
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        tmp = res

        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next
            else:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next
        tmp.next = l1 or l2
        return res.next
        '''
        #version 2.0
        l = len(lists)
        if l == 0:
            return None
        elif l == 1:
            return lists[0]
        elif l == 2:
            return self.mergeTwoLists(lists[0],lists[1])
        else:
            return self.mergeTwoLists(self.mergeKLists(lists[:l/2]),self.mergeKLists(lists[l/2:]))
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        tmp = res

        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next
            else:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next
        tmp.next = l1 or l2
        return res.next
