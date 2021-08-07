class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        min_len = min([len(s) for s in strs])

        if min_len == 0:
            return ''
        for i in range(min_len):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return strs[j][:i]
        return strs[0][:i + 1]


# Path: codes\14. Longest Common Prefix\code.py

            