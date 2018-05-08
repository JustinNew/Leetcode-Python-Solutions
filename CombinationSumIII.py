# 216. Combination Sum III

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        nums = [i + 1 for i in range(9)]
        result = []
        temp = []

        self.util(k, n, nums, temp, result)

        return result

    def util(self, k, n, nums, temp, result):

        if k == 1 and n in nums:
            result.append(temp + [n])
            return
        if k == 1 and n not in nums:
            return 

        for i in range(len(nums)):
            self.util(k - 1, n - nums[i], nums[i + 1:], temp + [nums[i]], result)

        return

if __name__ == '__main__':

    s = Solution()
    print(s.combinationSum3(3,9))
