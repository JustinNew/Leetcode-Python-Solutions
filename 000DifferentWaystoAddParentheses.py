# 241. Different Ways to Add Parentheses

class Solution(object):

    # Divide and Conquer.
    def diffWaysToCompute(self, input):

        if input.isdigit():
            return [int(input)]
        res = []

        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))

        return res
    
    def helper(self, m, n, op):

        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n

    # My codes.
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        if input[0] in ['+', '-', '*']:
            return [None]
        if input[-1]  in ['+', '-', '*']:
            return [None]

        s = 0
        e = 0
        l = []
        while e < len(input) - 1:
            if input[e] in ['+', '-', '*']:
                l.append(int(input[s:e]))
                l.append(input[e])
                s = e + 1

            e = e + 1
        
        l.append(int(input[s:e + 1]))

        def divide(nums):

            if len(nums) == 1:
                return nums

            temp = []
            for i in range(len(nums)):
                if nums[i] in ['+', '-', '*']:
                    left = divide(nums[:i])
                    right = divide(nums[i + 1:])
                    if nums[i] == '+':
                        temp += [j + k for j in left for k in right]
                    elif nums[i] == '-':
                        temp += [j - k for j in left for k in right]
                    else:
                        temp += [j * k for j in left for k in right]

            return temp

        return divide(l)
