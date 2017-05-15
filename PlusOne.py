class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits = digits[::-1]

        carry = 0
        for i in range(len(digits)):
            if i ==0:
                sum = carry + digits[i] + 1
            else:
                sum = carry + digits[i]
            carry = int(sum/10)
            digits[i] = int(sum%10)

        if carry != 0:
            digits.append(carry)

        return digits[::-1]
            
