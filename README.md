Python For Leetcode
==========

### How to solve a coding problem well:
  - Understand the problem well
  - Solve the problem on paper
  - Form clear logic
  - Turn the solution into code
  - Think about the test cases
  - Do the test cases for the code to test code

### Dynamic Programming

  - Problems can be solved like F(n) = F(n-1) + F(n-2)
  
There are three ways to do Dynamic Programming: 
  - Backtracking: recursively solving the problem
  - Top-down dynamic programming: build a memoization table to reduce computation, a way to optimize backtracking.
  - Bottom-up dynamic programming: top-down to bottom-up conversion is done by eliminating recursion.
  - A good example: https://leetcode.com/articles/jump-game/

Example problems:
- 62 Unique Paths
  
### Greedy

  - Problems can be solved like maxReach = max(maxReach, i+x), where i+x is current reach.
  
Example problems:
- 55 Jump Game

### Linked List

  - Remember to use Dummy Head Node to make life easier.
  - Use two points for many problems.

### Array/List problems

Trick
  - Two pointers
  - One or Two extra help arrays/lists: Trapping Rain Water, Product of Array Except Self 
  

## Algorithms

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

#### Find min in rotated sorted array

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
  
#### Rotate an array by k elements [1,2,3,4,5,6,7] by 3 into [5,6,7,1,2,3,4]
  - reverse the first n - k elements
  - reverse the rest of them
  - reverse the entire array

#### Two Sum Using Hash

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

#### Max sub array

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

#### Symmetric Tree

Solve it recursively.
  - root.left isMirror root.right
  - left.left isMirror right.right and left.right isMirror right.left
  
#### String permutation
    
Solve it recursively:
  - Try all n characters in the first position and reduce it to a n-1 characters permutation, ...
  - Combination is using two pointers.
  - Permutation is using one pointer.
  
#### Intersection of Two Linked Lists
    
At least three ways: 
  - Make a cycle in the list and find the cycle start
  - L1 + L2 and L2 + L1 should have the same ending
  - Let two pointers start from the places having the same distance from their end

#### Is Linked List Palidrome 
        
Reverse the second half of the linked list.
Note: 
  - Do change to part of the data.