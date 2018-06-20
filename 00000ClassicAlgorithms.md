## Median of two sorted arrays

https://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/

```python
def findMedianSortedArrays(self, A, B):
    
    l = len(A) + len(B)
    
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

def kth(self, a, b, k):
    
    if not a:
        return b[k]
    if not b:
        return a[k]
    
    ia, ib = len(a) // 2 , len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)
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
  - Using one conditional criteria: nums[mid] > nums[end], yes -> right; no -> left
  - Comparing with nums[start] does not work.
  
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

## 236 Lowest Common Ancestor of a Binary Tree

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

Get permutation of [1,2,3]
  - [[1]]
  - [[2,1], [1,2]]
  - [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2],[1,2,3]]

## Symmetric Tree

Solve it recursively.
  - root.left isMirror root.right
  - left.left isMirror right.right and left.right isMirror right.left
  
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
