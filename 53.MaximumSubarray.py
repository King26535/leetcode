class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        maxSofar, maxEndhere = nums[0], nums[0]
        for i in range(1,l):
            maxEndhere = max(maxEndhere + nums[i],nums[i])
            maxSofar = max(maxSofar,maxEndhere)
        return maxSofar
