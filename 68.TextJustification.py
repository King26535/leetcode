class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        #version 1.0 58ms
        '''
        def justify(temp, L, currl):
            l, res = len(temp)-1, temp[0]
            if l == 0:
                return res + ' '*(L - currl)
            rest, i = L - currl, 1
            while rest > 0:
                if rest%l == 0:
                    res += ' '*(rest/l) + temp[i]
                    rest = rest - rest/l
                else:
                    res += ' '*(rest/l+1) + temp[i]
                    rest = rest - (rest/l+1)
                i += 1
                l -= 1
            return res
            
        def justify1(temp, L, currl):
            l, res = len(temp)-1, temp[0]
            if l == 0:
                return res + ' '*(L - currl)
            rest, i = L - currl, 1
            while l > 0:
                res += ' ' + temp[i]
                rest -= 1
                i += 1
                l -= 1
            res += ' '*rest
            return res
        
        if maxWidth == 0:
            return words
        currl,temp,res = 0,[],[]
        for word in words :
            if currl + len(word) + len(temp) <= maxWidth:
                temp.append(word)
                currl += len(word)
            else:
                res.append(justify(temp,maxWidth,currl))
                temp = [word]
                currl = len(word)
        res.append(justify1(temp,maxWidth,currl))
        return res
        '''
        #verion 2.0 46ms
        '''
        def justify(temp, L, currl, mode):
            l, res = len(temp)-1, temp[0]
            if l == 0:
                return res + ' '*(L - currl)
            rest, i = L - currl, 1
            while l > 0:
                if mode == 0:
                    if rest%l == 0:
                        res += ' '*(rest/l) + temp[i]
                        rest = rest - rest/l
                    else:
                        res += ' '*(rest/l+1) + temp[i]
                        rest = rest - (rest/l+1)
                else:
                    res += ' ' + temp[i]
                    rest -= 1
                i += 1
                l -= 1
            return res if mode == 0 else res + ' '*rest
        
        if maxWidth == 0:
            return words
        currl,temp,res = 0,[],[]
        for word in words :
            if currl + len(word) + len(temp) <= maxWidth:
                temp.append(word)
                currl += len(word)
            else:
                res.append(justify(temp,maxWidth,currl,0))
                temp = [word]
                currl = len(word)
        res.append(justify(temp,maxWidth,currl,1))
        return res
        '''
        #version 3.0 72ms
        res, cur, number_of_letters = [], [], 0
        for word in words:
            if len(word) + len(cur) + number_of_letters > maxWidth:
                for i in range(maxWidth-number_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, number_of_letters = [], 0
            cur += [word]
            number_of_letters += len(word)
        return res + [' '.join(cur).ljust(maxWidth)]
