class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        '''
        #version 1.0
        temp = ''
        fac = [1]*n
        for i in range(n):
            temp += str(i+1)
        for i in range(1,n):
            fac[i] = fac[i-1]*i
        def permutation(nums,n,k):
            if k == 0 or n == 1:
                return nums
            return nums[k/fac[n-1]] + permutation(nums[:k/fac[n-1]] + nums[k/fac[n-1]+1:], n-1, k%fac[n-1])

        return permutation(temp,n,k-1)
        '''
        temp = ''
        fac = [1]*n
        for i in range(n):
            temp += str(i+1)
        for i in range(1,n):
            fac[i] = fac[i-1]*i
        k -= 1
        res = ''
        for i in range(n):
            index = k/fac[n-1-i]
            res += temp[index]
            temp = temp[:index] + temp[index+1:]
            k %= fac[n-1-i]
        return res
