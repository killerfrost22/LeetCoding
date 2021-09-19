class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1  or numRows>=len(s):
            return s
        L = []
        for i in range(numRows):
            L.append('')
        index = 0
        step = 1

        for j in s: 
            L[index] += j
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return ''.join(L)


