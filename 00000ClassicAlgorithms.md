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

Example Problems:
  - 162 Find Peak Element

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
