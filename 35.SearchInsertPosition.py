class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        lo,hi = 0,l-1
        if l == 0:
            return 0
        while lo < hi:
            mid = (lo + hi)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if nums[hi] < target:
            return hi + 1
        else:
            if hi < 0:
                return 0
            return hi
