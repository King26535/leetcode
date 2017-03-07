class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        #version 1.0 49 ms
        count = [0,0,0]
        for item in nums:
            count[item] += 1
        l = 0
        for i in xrange(3):
            if count[i] == 0:
                continue
            start = 0 if i == 0 else sum(count[:i])
            while l < count[i]:
                nums[start + l] = i
                l += 1
            l = 0
        '''
        '''
        #version 2.0 48ms
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        '''
        #version 3.0
        i, j = 0, 0
        for k in xrange(len(nums)):
            temp = nums[k]
            nums[k] = 2
            if temp < 2:
                nums[j] = 1
                j += 1
            if temp == 0:
                nums[i] = 0
                i += 1
