class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        l = len(nums)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if(nums[i] + nums[j] == target):
                    m = i
                    n = j
        return [m, n]
        '''
        temp = nums[:]
        temp.sort()
        result = []
        l,r = 0,len(temp)-1
        while l<r:
            if temp[l] + temp[r] == target:
                for i in range(len(nums)):
                    if temp[l] == nums[i]:
                        result.append(i)
                        break
                for j in range(len(nums)-1,-1,-1):
                    if temp[r] == nums[j]:
                        result.append(j)
                        break
                break
            elif temp[l] + temp[r] < target:
                l += 1
            else:
                r -= 1
        return result
