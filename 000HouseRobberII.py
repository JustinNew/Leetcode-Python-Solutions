# 213. House Robber II

# Get all the possible combination of robber lists.
# Find the max of these lists.
# Start 1    2    3
# []   []    []   []
#      [1]   [1]  [1]
#            [2]  [2]
#                 [3]
#                 [1,3]
#                  

class Solution(object):

    # Time Limit Exceeded.
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        com = [[]]
        for i in range(l):
            new = []
            for t_l in com:
                if len(t_l) != 0 and i != t_l[-1] + 1 and (i + 1) % l != t_l[0]:
                    new.append(t_l + [i])
                if len(t_l) == 0:
                    new.append([i])
            com += new

        m = 0
        for t_l in com:
            t = 0
            if len(t_l) != 0:
                for i in t_l:
                    t += nums[i]
                if t > m:
                    m = t

        return m

if __name__ == '__main__':

    s = Solution()
    print(s.rob())
