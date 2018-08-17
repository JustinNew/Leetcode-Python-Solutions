# 325. Maximum Size Subarray Sum Equals k

```
Given an Integer Array, find the maximum size of subarray whose sum equals to K.
For example, Given [1,2,-3,3,-1,2,4] and K=3, the subarray [1,2,-3,3] sum equals to 3.
```

# Facebook Tag

# Tricks:
# Use a dictionary to carry sum2pos.
# Update sum2pos only if it's a new sum.


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum2pos = {0:0}

        ans = None
        tsum = 0

        for i in xrange(len(nums)):

            tsum += nums[i]
            wanted = tsum - k
            if wanted in sum2pos:
                length = i + 1 - sum2pos[wanted]
                if ans is None or length > ans:
                    ans = length
            if tsum not in sum2pos:
                sum2pos[tsum] = i + 1

        return ans or 0

    def MaxSubArray(self, list, k):
        d = {}
        d[0] = -1
        s = 0
        result = 0
        for i in range(len(list)):
            s += list[i]
            if s not in d:
                d[s] = i
            if k - s in d:
                t = i - d[k - s]
                result = max(result, t)

        return result

if __name__ == '__main__':

    so = Solution()
    print(so.MaxSubArray([1,2,-3,3,-1,2,4], 3))
