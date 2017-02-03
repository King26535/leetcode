class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #version 1.0 45/52ms
        init = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res1,res2 = [''],[]
        if digits == "":
            return []
        for index in digits:
            for ch1 in res1:
                for ch2 in init[int(index)]:
                    res2.append(ch1 + ch2)
            res1 = res2
            res2 = []
        return res1
        
        '''#version 2.0 dfs 49/42ms
        if digits == "":
            return []
        alpha = [" ", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]  
        res = []  
        word = []  
        def dfs(cur):  
            if cur >= len(digits):  
                res.append(''.join(word))  
            else:  
                for x in alpha[(int)(digits[cur]) - (int)('0')]:  
                    word.append(x)  
                    dfs(cur + 1)  
                    word.pop()  
        dfs(0)  
        return res
        '''
        '''#version 3.0 recursion 59/39ms 
        if digits == '':
            return []
        self.DigitDict=[' ','1', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = ['']
            
        for d in digits:
            res = self.letterCombBT(int(d),res)
        return res
            
    def letterCombBT(self, digit, oldStrList):
        return [dstr+i for i in self.DigitDict[digit] for dstr in oldStrList]
        '''
