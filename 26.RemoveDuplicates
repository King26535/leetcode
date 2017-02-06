class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,id = len(nums),1
        if l < 2:
            return l
        for i in range(1,l):
            if nums[i] != nums[i-1]:
                nums[id] = nums[i]
                id += 1
        return id
