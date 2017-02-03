class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums.sort()
        result=nums[0]+nums[1]+nums[2]
        for i in xrange(len(nums)-2):
            j,k = i+1,len(nums)-1
            while j<k:
                temp=nums[i]+nums[j]+nums[k]
                if abs(temp-target)<abs(result-target):
                    result=temp 
                if temp<target:
                    j+=1
                elif temp>target:
                    k-=1
                else:
                    return target
        return result
