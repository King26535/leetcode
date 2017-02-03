class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''#version 1.0 TLE
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    temp = [nums[i],nums[j],nums[k]]
                    if sum(temp)==0 and temp not in result:
                        result.append(temp)
                        break
        return result
        
        '''
        '''#version 2.0
        nums.sort()
        res=[]
        if len(nums)<3:
            return[]
        for start in xrange(len(nums)-2):
            if nums[start]>0:
                break
            if start>0 and nums[start]==nums[start-1]:
                continue
            res=self.twoSum(nums,start,res)
        return res
    
    def twoSum(self,nums,start,res):
        dict={}
        target=-nums[start]
        for i in xrange(start+1,len(nums)):
            if target-nums[i] in dict:
                temp=[-target,nums[i],target-nums[i]]
                temp.sort()
                if temp not in res:
                    res.append(temp)
                continue
            dict[nums[i]]=i
        return res
        '''
        #version 3.0
        nums.sort()
        res=[]
        for i in xrange(len(nums)-2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i]!=nums[i-1]:
                l,r = i+1,len(nums)-1
                while l<r:
                    if nums[l] + nums[r] == -nums[i]:
                        res.append([nums[i],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < -nums[i]:
                        l += 1
                    else:
                        r -= 1
            else:
                continue
        return res
