# 319. Bulb Switcher

'''
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.
'''

class Solution(object):
    # Time Limit Exceeded: test case 9999
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        result = 1
        for i in range(2, n + 1):
            count = 1
            for j in range(2, i + 1):
                if i % j == 0:
                    count += 1
            if count % 2 == 1:
                result += 1

        return result

    # Borrow idea from prime numbers.
    # Time Limit Exceeded: test case 999999
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        dp = [1 for i in range(n + 1)]
        dp[0] = 0

        for step in range(2, n + 1):
            start = 0
            while start + step <= n:
                start = start + step
                if dp[start] == 0:
                    dp[start] = 1
                elif dp[start] == 1:
                    dp[start] = 0

        return sum(dp)

    # Only numbers of perfect square remains.
    # 9: 1, 3, 9
    # 16: 1, 2, 4, 8, 16
    # Prime numbers always two times operation: 1 and n, it's off
    # Not perfect square numbers always even time operations, it's off
    # Only perfect square numbers have odd time operations, it's on
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        result = 0
        step = 1
        while step * step <= n:
            result += 1
            step += 1

        return result
