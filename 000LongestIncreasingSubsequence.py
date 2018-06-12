# 300. Longest Increasing Subsequence

class Solution:

    # My solution.
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        # To avoid Time Limit Exceeded.
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                flag = 1
        if flag == 0:
            return len(nums)

        result = {}
        result[1] = [nums[0]]

        for i in range(1, len(nums)):
            temp = {k:v for (k, v) in result.items()}
            for lgth in result:
                if nums[i] < result[1][0]:
                    temp[1] = [nums[i]]
                elif nums[i] > result[lgth][-1]:
                    if lgth + 1 in result and nums[i] < result[lgth + 1][-1]:
                        temp[lgth + 1] = result[lgth] + [nums[i]]
                    elif lgth + 1 not in result:
                        temp[lgth + 1] = result[lgth] + [nums[i]]

            result = temp

        return max(result.keys())

    # Dynamic Programming.
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        lis = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1

        return max(lis)

if __name__ == '__main__':

    so = Solution()
    print(so.lengthOfLIS([1,2,3,4,5,6,7,8,9,10]))
