class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        #version 1.0 dict
        if words == []:
            return []
        word_size = len(words)
        word_length = len(words[0])
        t = word_size * word_length
        word_map = {}
        res = []
        for word in words:
            if word not in word_map:
                word_map[word] = 1
            else:
                word_map[word] += 1
        for i in xrange(len(s)-t+1):
            j = 0
            temp_map = {}
            while j < word_size:
                word = s[i+j*word_length:i+(j+1)*word_length]
                if word not in word_map:
                    break
                if word not in temp_map:
                    temp_map[word] = 1
                else:
                    temp_map[word] += 1
                if temp_map[word] > word_map[word]:
                    break
                j += 1
            if j == word_size:
                res.append(i)
        return res
        
        '''#Error,???different results between here and IDE
        word_size = len(words)
        word_length = len(words[0])
        t = word_size * word_length
        hashsum = sum([abs(hash(x)) for x in words])
        h = [abs(hash(s[i:i+word_length]))*(s[i:i+word_length] in words) for i in xrange(len(s)-word_length+1)]
        return [i for i in xrange(len(s)-t+1) if sum(h[i:i+t:word_length]) == hashsum]
        '''
