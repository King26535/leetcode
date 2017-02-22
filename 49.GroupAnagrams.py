class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for item in strs:
            temp = ''.join(sorted(item)) #important
            if temp not in dict:
                dict[temp] = [item]
            else:
                dict[temp].append(item)
        return [dict[item] for item in dict]
