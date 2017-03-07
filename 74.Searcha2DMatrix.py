class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        m,n = len(matrix),len(matrix[0])
        l,r = 0,m*n - 1
        while l <= r:
            mid = (l+r)/2
            num = matrix[mid/n][mid%n]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        '''
        if len(matrix) == 0:
            return False
        elif len(matrix[0]) == 0:
            return False
        m,n = len(matrix),len(matrix[0])
        l,r = 0,m*n - 1
        while l < r:
            mid = (l + r -1)/2
            if matrix[mid/n][mid%n] < target:
                l = mid + 1
            else:
                r = mid
        return matrix[r/n][r%n] == target
        '''
        '''
        if matrix == []:
            return False
        up,down = 0,len(matrix)-1
        left,right = 0,len(matrix[0])-1
        while up < down:
            mid = (up+down)/2 + 1
            if target < matrix[mid][0]:
                down = mid - 1
            elif target > matrix[mid][0]:
                up = mid
            else:
                return True
        while left <= right:
            mid = (right+left)/2
            if target == matrix[up][mid]:
                return True
            elif target < matrix[up][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
        '''
        
