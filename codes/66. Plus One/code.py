class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1 and digits[0] == 9:
            return [1,0]
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits = self.plusOne(digits[:-1])
            digits.append(0)

        return digits
            
