class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if(nums[i] + nums[j] == target):
                    m = i
                    n = j
        return [m, n]
