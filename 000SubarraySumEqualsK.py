# 560. Subarray Sum Equals K

class Solution:

    # Intuition
    # Time Limit Exceeded.
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        l = [0 for i in nums]
        result = 0

        for i in range(len(nums)):
            for j in range(i + 1):
                l[j] += nums[i]
                if l[j] == k:
                    result += 1

        return result

    # Key is continuous    
    # Get the SumSoFar list.
    # Then it's a two sum problem.
    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = []
        s = 0
        for i in nums:
            s += i
            l.append(s)

        d = {}
        result = 0
        for i in range(len(l)):
            if l[i] == k:
                result += 1
            if l[i] in d:
                result += d[l[i]]

            if l[i] + k in d:
                d[l[i] + k] += 1
            else:
                d[l[i] + k] = 1

        return result

if __name__ == '__main__':

    so = Solution()
    print(so.subarraySum1([1, -1, 1, -1], 0))
