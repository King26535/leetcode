class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''#version 1.0
        new = nums1 + nums2
        new.sort()
        l = len(new)
        return (new[(l-1)/2]+new[l/2])/2.0
        '''
        #version 2.0, to find the kth item
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l//2)
        else:
            return (self.kth(nums1, nums2, l//2) + self.kth(nums1, nums2, l//2-1)) / 2.0
            
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
            
        ia, ib = len(a)//2, len(b)//2
        va, vb = a[ia], b[ib]
        
        if ia + ib < k:
            if va > vb:
                return self.kth(a, b[ib+1:], k-ib-1)
            else:
                return self.kth(a[ia+1:], b, k-ia-1)
        else:
            if va > vb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
