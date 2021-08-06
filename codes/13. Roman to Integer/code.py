class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_romans ={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        # num = 0 
        # value = 0
        n = len(s)
        value = 0
        for i in range(n):
            if i < n-1 and map_romans[s[i]] < map_romans[s[i+1]]:
                value -= map_romans[s[i]]
            else:
                value += map_romans[s[i]]
        return value

