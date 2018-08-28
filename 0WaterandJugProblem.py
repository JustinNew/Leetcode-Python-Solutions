# 365. Water and Jug Problem

# A math problem
# Or a brain teaser problem
# Use gcd(a, b)
# The basic idea is to use the property of Bézout's identity and check if z is a multiple of GCD(x, y)
# https://leetcode.com/problems/water-and-jug-problem/discuss/83715/Math-solution-Java-solution 
# https://leetcode.com/problems/water-and-jug-problem/discuss/83720/Clear-Explanation-of-Why-Using-GCD

class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        if x + y < z:
            return False

        if x == z or y == z or x + y == z:
            return True

        def gcd(a, b):
            while b != 0:
                temp = b
                b = a % b
                a = temp
            return a

        return z % gcd(x, y) == 0
        
