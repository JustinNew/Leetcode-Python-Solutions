# 134. Gas Station

# Tricky Math Problem.
# If total gas is greater than total cost, there is a solution.
# Whenever the sum is negative, reset it and let the car start from next point.
# In the mean time, add up all of the left gas to total. If it’s negative finally, return -1 since it’s impossible to finish.
# If it’s non-negative, return the last point saved in res;

class Solution(object):

    # Time Limit Exceeded.
    def canCompleteCircuit1(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        net = [i - j for i, j in zip(gas, cost)]

        l = len(gas)

        for i in range(l):
            count = 0
            s = 0
            if net[i] < 0:
                continue
            while count < l:
                s += net[(count + i)%l]
                if s < 0:
                    break
                count += 1
            if count == l:
                return i

        return -1

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1
        position = 0
        balance = 0 # current tank balance
        for i in range(len(gas)):
            balance += gas[i] - cost[i] # update balance
            if balance < 0: # balance drops to negative, reset the start position
                balance = 0
                position = i+1
        return position

