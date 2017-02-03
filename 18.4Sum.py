class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #version1.0 dict and map
        nums.sort()
        dict,res,maxlen = {},set(),len(nums)
        for i in range(maxlen-1):
            for j in range(i+1,maxlen):
                if nums[i] + nums[j] not in dict:
                    dict[nums[i] + nums[j]] = [(i,j)]
                else:
                    dict[nums[i] + nums[j]].append((i,j))
        for i in range(maxlen-3):
            for j in range(i+1,maxlen-2):
                T = target - nums[i] - nums[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j:
                            res.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return [list(i) for i in res]
        '''
        #version 2.0 N^3 1s
        res,maxlen = [],len(nums)
        nums.sort()
        for i in range(maxlen-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,maxlen-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l,r = j+1,maxlen-1
                T = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == T:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < T:
                        l += 1
                    else:
                        r -= 1
        return res
        '''
