class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if needle not in haystack:
            return -1 
        else:
            return haystack.index(needle)

        # runtime: O(n)