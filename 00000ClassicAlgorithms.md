## Median of two sorted arrays

https://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/

```python
def findMedianSortedArrays(self, A, B):
    
    l = len(A) + len(B)
    
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

# Kth is '0' based.
def kth(nums1, nums2, k):

    if not nums1:
        return nums2[k]
    elif not nums2:
        return nums1[k]

    m1 = int(len(nums1) / 2)
    m2 = int(len(nums2) / 2)

    if m1 + m2 < k:
        if nums1[m1] < nums2[m2]:
            # nums1[m1] can not be medium.
            return kth(nums1[m1 + 1:], nums2, k - m1 - 1)
        else:
            return kth(nums1, nums2[m2 + 1:], k - m2 - 1)
    else:
        if nums1[m1] < nums2[m2]:
            # nums2[m2] can not be medium.
            return kth(nums1, nums2[:m2], k)
        else:
            return kth(nums1[:m1], nums2, k)
```

## Maximum Size Subarray Sum Equals k


Tricks:
  - Use a dictionary to carry sum2pos.
  - Update sum2pos only if it's a new sum.
  - Use a dictionary is also the trick to do 2Sum.

```python
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
```

#### add without +

  - sum = a^b
  - carry = (a&b) << 1
  - recursive call this until carry == 0

#### Binary Search

Note: 
  - low=0, high = len(nums)-1
  - low <= high

```python
low = 0
high = len(nums) - 1
        
while low <= high:
    mid = (low+high)//2
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        low = mid + 1
    else:
        high = mid - 1
```

## Find min in rotated sorted array

```python
        start = 0
        end = len(nums) - 1
        while start < end:
            m = start + (end - start) / 2
            if nums[m] > nums[end]:
                start = m + 1
            else:
                end = m
        return nums[start]
```
Note: 
  - Use one conditional criteria: nums[mid] > nums[end], yes -> right; no -> left
  - Comparing with nums[start] does not work.
  - Use **'<'** instead of **'<='** compared to binary search  
  - **start = m + 1** and **end = m** compared to **low = m + 1** and **high = m - 1**
  - The start and high assignment is very imilar in problem "162 Find Peak Element"

## Course Schedule

To see whether there is circle in the graph.
  - 1 if node v has not been visited, then mark it as 0.
  - 2 if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
  - 3 if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.

```python
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True
```

## Rotate an array by k elements [1,2,3,4,5,6,7] by 3 into [5,6,7,1,2,3,4]
  - reverse the first n - k elements
  - reverse the rest of them
  - reverse the entire array

## Two Sum Using Hash

```python
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i
            else:
                return map[num[i]], i

        return -1, -1
```

## Max sub array

```python
def maxSubArray(self, A):
    if not A:
        return 0

    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum
```

## Linked List Cycle II

```python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        fast = head
        slow = head

        while slow.next and fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
            
        if not slow.next or not fast.next or not fast.next.next:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
```
Note:
  - After find a meeting place, the next time **slow** and **fast** both move one step at a time. 

## Reservoir Sampling

```sh
Init : a reservoir with the size： k  
  
for i= k+1 to N  
  
    M=random(1, i);  
  
    if( M < k)  
  
     SWAP the Mth value and ith value  
  
end for
```

## Find Median from Data Stream

## Permuation without recursion
The basic idea is, to permute n numbers, we can add the nth number into the resulting List<List<Integer>> from the n-1 numbers, in every possible position.

## Permutation

Get permutation of [1,2,3]
  - [[1]]
  - [[2,1], [1,2]]
  - [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2],[1,2,3]]

Permuation is actually swapping.
The following code gets a random shuffle of list.
```python
    def shuffle(nums):
        ans = nums[:]                     # copy list
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index 
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans
```

## Symmetric Tree

Solve it recursively.
  - root.left isMirror root.right
  - left.left isMirror right.right and left.right isMirror right.left
  
## Lowest Common Ancestor of a Binary Tree 

Algorithm:
  - Need to traversal the binary tree
  - recursively BFS travesal and feed back the result

```python
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        elif left:
            return left
        else:
            return right
```

## String permutation
    
Solve it recursively:
  - Try all n characters in the first position and reduce it to a n-1 characters permutation, ...
  - Combination is using two pointers.
  - Permutation is using one pointer.
  
## Intersection of Two Linked Lists
    
At least three ways: 
  - Make a cycle in the list and find the cycle start
  - L1 + L2 and L2 + L1 should have the same ending
  - Let two pointers start from the places having the same distance from their end

## Is Linked List Palidrome 
        
Reverse the second half of the linked list.

Note: 
  - Do change to part of the data.

## Longest Increasing Subsequence

'''
tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
len = 3   :      [4, 5, 6]            => tails[2] = 6

We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

Each time we only do one of the two:

(1) if x is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]
Doing so will maintain the tails invariant. The the final answer is just the size.
'''
def lengthOfLIS(self, nums):
    def search(temp, left, right, target):
        if left == right:
            return left
        mid = left+(right-left)/2
        return search(temp, mid+1, right, target) if temp[mid]<target else search(temp, left, mid, target)
    temp = []
    for num in nums:
        pos = search(temp, 0, len(temp), num)
        if pos >=len(temp):
            temp.append(num)
        else:
            temp[pos]=num
    return len(temp)

## Largest Rectangle in Histogram

'''
The stack maintain the indexes of buildings with ascending height. 
Before adding a new building pop the building who is taller than the new one. 
The building popped out represent the height of a rectangle with the new building 
as the right boundary and the current stack top as the left boundary. 
Calculate its area and update ans of maximum area. 
Boundary is handled using dummy buildings.

1. Using stack to only keep increasing sequence.
2. When find an element smaller, calculate the rectangle area.
'''

    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

## Reservior Sampling

[This blog](https://gregable.com/2007/10/reservoir-sampling.html) explains the reservior sampling very well.

examples:
  - 382 Linked List Random Node
