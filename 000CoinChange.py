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

    # Try bottom up BFS and build a table.
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

if __name__ == '__main__':

    so = Solution()
    print(so.coinChange2([27,398,90,323,454,413,70,315], 6131))
