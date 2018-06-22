# 322. Coin Change

# BFS
# Silimar to 279 Perfect Squares

class Solution:

    # Time Limit Exceeded.
    # There is repeated calculations in BFS.
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        count = 0
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0

        amounts = [amount]
        while True:

            temp = []
            count += 1
            for i in amounts:
                for j in coins:
                    if i > j and i - j not in temp:
                        temp.append(i - j)
                    if i == j:
                        return count

            if len(temp) == 0:
                return -1

            amounts = temp

    # Optimization
    # Improve the speed by adding visited list.
    # Remove the 'i - j in temp', this is time consuming.
    def coinChangeBFSTopDown(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        count = 0
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0

        visited = [False for i in range(amount+1)]
        visited[amount] = True
        amounts = [amount]
        while True:

            temp = []
            count += 1
            for i in amounts:
                for j in coins:
                    if i > j and not visited[i - j]:
                        temp.append(i - j)
                        visited[i - j] = True
                    if i == j:
                        return count

            if len(temp) == 0:
                return -1

            amounts = temp

    # Try bottom up BFS and build a table.
    # Time limit exceeded.
    # Actually the same as Top Down.
    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        if amount in coins:
            return 1

        # Create a dictionary to keep BFS buildup.
        d = {i:1 for i in coins}

        while True:

            temp = {}
            for i in d:
                for j in coins:
                    if i + j == amount:
                        return d[i] + 1
                    if i + j not in d:
                        temp[i + j] = d[i] + 1

            if min(temp.keys()) > amount:
                return -1

            d.update(temp)

    # Optimization
    # BFS Bottom up.
    # Improve TLE by removing 'i + j not in d'
    def coinChangeBFSBottomUP(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        if amount in coins:
            return 1

        # Create a dictionary to keep BFS buildup.
        d = [0]
        visited = [False for i in range(amount + 1)]
        visited[0] = True
        count = 0
        
        while True:

            count += 1
            temp = []
            for i in d:
                for j in coins:
                    if i + j == amount:
                        return count
                    if i + j < amount and not visited[i + j]:
                        temp.append(i + j)
                        visited[i + j] = True

            if len(temp) == 0:
                return -1

            d = temp

    # Bottom Up + Top Down
    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        if amount in coins:
            return 1

        # Create a dictionary to keep BFS buildup.
        bottomup = {i:1 for i in coins}

        topdown = {amount: 0}
        
        while True:

            temp1 = {}
            temp2 = {}

            # Top Down.
            for i in topdown:
                if i in bottomup:
                    return topdown[i] + bottomup[i]
                for j in coins:
                    if i - j == 0:
                        return topdown[i] + 1
                    if i > j and i - j not in topdown:
                        temp1[i - j] = topdown[i] + 1

            if len(temp1) == 0:
                return -1
            topdown.update(temp1)

            # Bottom Up.
            for i in bottomup:
                if i in topdown:
                    return topdown[i] + bottomup[i]
                for j in coins:
                    if i + j == amount:
                        return bottomup[i] + 1
                    if i + j not in bottomup:
                        temp2[i + j] = bottomup[i] + 1

            if max(temp1) < min(temp2):
                return -1
            bottomup.update(temp2)


    # Optimization of Top Down + Bottom Up.
    def coinChangeTopBottom(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        if amount in coins:
            return 1

        topdown = [False for i in range(amount + 1)]
        bottomup = [False for i in range(amount + 1)]
        topdown[amount] = True
        bottomup[0] = True
        top = [amount]
        bottom = [0]

        top_count, bottom_count = 0, 0
        while True:

            t1 = []
            t2 = []

            for i in top:
                if bottomup[i]:
                    return top_count + bottom_count
                for coin in coins:
                    if i - coin >= 0 and bottomup[i - coin]:
                        return top_count + bottom_count + 1
                    if i - coin >= 0 and not topdown[i - coin]:
                        topdown[i - coin] = True                            
                        t1.append(i - coin)
            if len(t1) > 0:
                top = t1
                top_count += 1

            for j in bottom:
                if topdown[j]:
                    return top_count + bottom_count
                for coin in coins:
                    if j + coin <= amount and topdown[j + coin]:
                        return top_count + bottom_count + 1
                    if j + coin <= amount and not bottomup[j + coin]:                         
                        bottomup[j + coin] = True
                        t2.append(j + coin)
                            
            if len(t2) > 0: 
                bottom_count += 1
                bottom = t2
            
            if len(t1) == 0 or len(t2) == 0:
                return -1


# Dynamic Programming
# Assume dp[i] is the fewest number of coins making up amount i, 
# then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
    # My DP
    def coinChangeTopBottom(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        if amount in coins:
            return 1

        MAX = float('inf')

        dp = [MAX for i in range(amount + 1)]

        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - j] + 1 for j in coins if i - j >= 0])

        if dp[-1] == MAX:
            return -1
        else:
            return dp[-1] 
