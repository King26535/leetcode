class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l,id = len(nums),0
        for i in range(l):
            if nums[i] != val:
                nums[id] = nums[i]
                id += 1
        return id
