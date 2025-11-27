class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashtb = {}
        for i in strs:
            tmp = i
            sort = "".join(sorted(tmp))
            if sort not in hashtb:
                hashtb[sort] = []
            hashtb[sort].append(i)
        ans = list(hashtb.values())
        return ans