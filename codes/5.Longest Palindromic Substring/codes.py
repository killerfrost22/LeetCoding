from unittest import result


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        result = ""
        for i in range(len(s)):
            result = max(self.helper(s,i,i)), self.helper(s,i,i+1),result, key=len)
        return result

    def helper(self,s,l,r):
        while 0<=l and r < len(s) and s[l] == s[r]:
            l-=1; r+=1
        return s[l+1:r]


