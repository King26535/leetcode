class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        init = [['','I','II','III','IV','V','VI','VII','VIII','IX'],
                ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
                ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
                ['','M','MM','MMM']]
        result += init[3][num/1000%10]
        result += init[2][num/100%10]
        result += init[1][num/10%10]
        result += init[0][num%10]
        
        return result
