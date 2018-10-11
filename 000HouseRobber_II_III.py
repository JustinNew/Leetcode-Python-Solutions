# 198. House Robber

class Solution:

'''
"determine the maximum amount of money you can rob" -> Max -> Dynamic Programming

dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])
'''

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)

        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        elif l == 2:
            return max(nums)

        dp = [0 for i in range(l)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, l):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

# 213. House Robber II 

'''
For House Robber II:
Either skip the first one or the last one, and then get the max of two results
1. Use 192 Hourse Robber for nums[:-1]
2. Use 192 House Robber for nums[1:]
3. max(rob1, rob2)
'''

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = len(nums)
        if m == 0:
            return 0
        elif m == 1:
            return nums[0]
        elif m == 2:
            return max(nums[0], nums[1])
        
        def util(arr):
 
            l = len(arr)
            if l == 0:
                return 0
            elif l == 1:
                return arr[0]
            elif l == 2:
                return max(arr)
 
            dp = [0 for i in range(l)]
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
 
            for i in range(2, l):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])  
 
            return dp[-1]
 
        return max(util(nums[:-1]), util(nums[1:]))

# 337. House Robber III

'''
     3
    / \
   2   3
    \   \ 
     3   1

Recursively:
1. From root, res = max(include_root, not_include_root)
2. include_root = root + left.not_include_root + right.not_include_root
3. not_include_root = max(left.include_root, left.not_include_root+ + max(right.include_root, right.not_include_root)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def util(n):
            if not n:
                return (0, 0)
            elif not n.left and not n.right:
                return (n.val, 0)

            nums1 = util(n.left)
            nums2 = util(n.right)

            include = n.val + nums1[1] + nums2[1]
            not_include = max(nums1[0], nums1[1]) + max(nums2[0], nums2[1])

            return (include, not_include)

        return max(util(root)[0], util(root)[1])
