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
  
### Binary Search

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

#### Find min in rotated sorted array:

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
