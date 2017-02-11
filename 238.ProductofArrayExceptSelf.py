class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #version 1.0 TLE
        '''
        res = []
        for i in range(len(nums)):
            left,right = 0,len(nums)-1
            lp,rp = 1,1
            while left < i:
                lp *= nums[left]
                left += 1
            while right > i:
                rp *= nums[right]
                right -= 1
            res += [lp*rp]
        return res
        '''
        #version 2.0
        res = [1] * len(nums)
        left,right = 1,1
        for i in range(len(nums)-1):
            left *= nums[i]
            res[i+1] *= left
        for i in range(len(nums)-1,0,-1):
            right *= nums[i]
            res[i-1] *= right
        return res
