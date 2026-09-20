class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for word in strs:
            sort = "".join(sorted(word))
            if sort in dict:
                dict[sort].append(word)
            else:
                dict[sort] = [word]
        return list(dict.values())
                
            