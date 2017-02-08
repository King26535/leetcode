class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #version1.0
        '''
        if len(nums) == 0:
            return -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
        '''
        #version 2.0
        l = len(nums)
        if l == 0:
            return -1
        lo,hi = 0,l-1
        while lo < hi:
            mid = (lo + hi)/2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        rot = lo
        lo,hi = 0,l-1
        while lo <= hi:
            mid = (lo + hi)/2
            realmid = (mid + rot)%l
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
