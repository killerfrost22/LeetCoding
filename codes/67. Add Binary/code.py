class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ''
        for i in range(max(len(a), len(b))):    
            if i < len(a):
                carry += int(a[len(a)-1-i])
            if i < len(b):
                carry += int(b[len(b)-1-i])
            result += str(carry % 2)
            carry //= 2
        if carry:
            result += str(carry)
        return result[::-1]
        