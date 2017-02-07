class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 2:
            return
        i = l-2
        while i >= 0:
            if nums[i] >= nums[i+1]:
                i -= 1
            else:
                break
        if i == -1:
            nums.reverse()
            return
        min_left = nums[i+1]
        index = i+1
        for j in range(i+1,l):
            if nums[j] > nums[i] and nums[j] < min_left:
                min_left = nums[j]
                index = j
        nums[index] = nums[i]
        nums[i] = min_left
        #def sort()
        for k in range(i+1,l-1):
            for m in range(k+1,l):
                if nums[k] > nums[m]:
                    temp = nums[k]
                    nums[k] = nums[m]
                    nums[m] = temp
        return
