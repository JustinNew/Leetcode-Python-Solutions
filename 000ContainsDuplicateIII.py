# 220. Contains Duplicate III

'''
Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
'''

'''
Of course, we need to compare num[i] with previouse k nums. if the difference is not greater than t, we return True.

A straight-foward solution is to compute the differences one by one, which needs at most k operations, so the total time is O(nk).

How to make it faster? We can store the previous nums in another way, i.e., in buckets according to their value, so that the comparisons perform only in ajdacent buckets.

The size of a bucket needs to be carefully set. If too large or too small, it can't work. We can set it to (t+1), so that the difference between any two nums in the bucket is at most t. For example, if t=5, the bucket size is set to 6. And for a num = 14, it should be put into #2 (14//6=2) bucket. This is an application of the pegion hole principle.

In this way, when num[i] comes, we compute its bucket b, and if b has been occupied by a previous num, it means the difference is at most t, and we return True. Also, we check b+1 and b-1 bucket to see the differences between the previous two and num[i], while other bucket needn't to be checked since the differences between nums in those bucket and num[i] are larger than t.
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        #TLE:
        '''for i in range(len(nums)):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(nums[i]-nums[j]) <= t:
                    return True
        return False'''

        if t < 0 or k <= 0:
            return False
        s = {}
        for i in range(len(nums)):
            if i-k-1>=0 and nums[i-k-1]//(t+1) in s:
                s.pop(nums[i-k-1]//(t+1))
            b = nums[i]//(t+1)
            if b not in s:
                s[b] = nums[i]
                if b+1 in s and abs(s[b+1]-s[b]) <= t:
                    return True
                if b-1 in s and abs(s[b-1]-s[b]) <= t:
                    return True
            else:
                return True
        return False
