# 334. Increasing Triplet Subsequence

class Solution:
    # DP
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
       
        if len(nums) < 3:
            return False

        dp = [1 for i in nums]
        for i in range(len(nums)): 
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    if dp[i] == 3:
                        return True

        return False

    # Binary Search
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def search(temp, left, right, target):
            if left == right:
                return left
            mid = left+int((right-left)/2)
            return search(temp, mid+1, right, target) if temp[mid]<target else search(temp, left, mid, target)
        temp = []
        for num in nums:
            pos = search(temp, 0, len(temp), num)
            if pos >=len(temp):
                temp.append(num)
                if len(temp) == 3:
                    return True
            else:
                temp[pos]=num
        return False

    # Same idea of Binary Search of LIS but simple
    def increasingTriplet(nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
