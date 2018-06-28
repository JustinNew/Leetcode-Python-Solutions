# 494. Target Sum

class Solution:

    # Recursive.
    # Time Limit Exceeded.
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        if not nums:
            return 0

        ways = []

        def util(nums, cur, S, ways):

            if cur == len(nums) and S == 0:
                ways.append(1)
                return
            if sum(nums[cur:]) < abs(S):
                return

            util(nums, cur + 1, S + nums[cur], ways)
            util(nums, cur + 1, S - nums[cur], ways)

            return

        util(nums, 0, S, ways)
        return sum(ways)

    # DFS
    def findTargetSumWays2(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        if not nums:
            return 0

        def dfs(nums, cur, S, ways):

            if cur == len(nums) and S == 0:
                ways.append(1)
                return
            if sum(nums[cur:]) < abs(S):
                return 

            for i in [-1, 1]:
                dfs(nums, cur + 1, S + i * nums[cur], ways)

            return

        dfs(nums, 0, S, ways)
        return sum(ways)

    # DP
    # DP(n, S) = DP(n - 1, S - nums[n - 1]) + DP(n - 1, S + nums[n - 1])
    # [1,1,1,1,1]
    # [1], DP[-1] = 1, DP[1] = 1
    # [1,1], DP[-2] = 1, DP[0] = 2, DP[2] = 1
    # ...
 
    def findTargetSumWays3(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        if not nums:
            return 0

        dp = {}
        dp[nums[0]] = 1
        if -1 * nums[0] in dp:
            dp[nums[0]] = 2
        else:
            dp[-1 * nums[0]] = 1

        for i in range(1, len(nums)):
            temp = {}
            for j in dp:
                if j + nums[i] in temp:
                    temp[j + nums[i]] += dp[j]
                else:  
                    temp[j + nums[i]] = dp[j]
                if j - nums[i] in temp:
                    temp[j - nums[i]] += dp[j]
                else:
                    temp[j - nums[i]] = dp[j]
            dp = {k:v for k, v in temp.items()}

        if S in dp:
            return dp[S]
        else:
            return 0       
 
if __name__ == '__main__':

    so = Solution()
    print(so.findTargetSumWays3([10,9,6,4,19,0,41,30,27,15,14,39,33,7,34,17,24,46,2,46], 45))
