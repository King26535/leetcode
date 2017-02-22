class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == []:
            return res
        rowStart,rowEnd,colStart,colEnd = 0,len(matrix)-1,0,len(matrix[0])-1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart,colEnd+1):
                res += [matrix[rowStart][i]]
            rowStart += 1
            
            for j in range(rowStart,rowEnd+1):
                res += [matrix[j][colEnd]]
            colEnd -= 1
            
            if rowStart <= rowEnd:
                for i in range(colEnd,colStart-1,-1):
                    res += [matrix[rowEnd][i]]
                rowEnd -= 1
            
            if colStart <= colEnd:
                for j in range(rowEnd,rowStart-1,-1):
                    res += [matrix[j][colStart]]
                colStart += 1
        return res
