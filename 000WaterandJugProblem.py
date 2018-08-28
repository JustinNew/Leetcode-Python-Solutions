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


    # For each jug, there are four actions:
    # 1. Fill up
    # 2. Empty
    # 3. Pour to other 
    # BFS search

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        if x > y:
            temp = x;
            x = y;
            y = temp;
            
        if z > x + y:
            return False;
        
        # set the initial state will empty jars;
        queue = [(0, 0)];
        visited = set((0, 0));
        while len(queue) > 0:
            a, b = queue.pop(0);
            if a + b == z:
                return True;
            
            states = set()
            
            states.add((x, b)) # fill jar x;
            states.add((a, y)) # fill jar y;
            states.add((0, b)) # empty jar x;
            states.add((a, 0)) # empty jar y;
            states.add((min(x, b + a), 0 if b < x - a else b - (x - a))) # pour jar y to x;
            states.add((0 if a + b < y else a - (y - b), min(b + a, y))) # pour jar x to y;

            for state in states:
                if state in visited:
                    continue;
                queue.append(state)
                visited.add(state);
                
        return False;        
