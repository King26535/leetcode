class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        lo,hi = 0,l-1
        res = [-1,-1]
        if l == 0:
            return res
        while lo < hi:
            mid = (lo + hi)/2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if nums[lo] != target:
            return res
        else:
            res[0] = lo
        hi = l-1
        while lo < hi:
            mid = (lo + hi)/2 + 1
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        res[1] = hi
        return res
