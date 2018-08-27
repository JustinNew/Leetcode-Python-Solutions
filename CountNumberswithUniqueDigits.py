# 357. Count Numbers with Unique Digits

'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 1

        result = []
        result.append(10)
        result.append(9 * 9)
        result.append(9 * 9 * 8)
        result.append(9 * 9 * 8 * 7) 
        result.append(9 * 9 * 8 * 7 * 6) 
        result.append(9 * 9 * 8 * 7 * 6 * 5) 
        result.append(9 * 9 * 8 * 7 * 6 * 5 * 4) 
        result.append(9 * 9 * 8 * 7 * 6 * 5 * 4 * 3) 
        result.append(9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2) 
        result.append(9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1) 

        if n >= 10:
            return sum(result)
    
        return sum(result[:n])
