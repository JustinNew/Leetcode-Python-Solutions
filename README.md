Python For Leetcode
==========

### How to solve a coding problem well:

  - Understand the problem well
  - Solve the problem on paper
  - Form clear logic
  - Turn the solution into code
  - Think about the test cases
  - Do the test cases for the code to test code
  - Use algorithms well known and understood to sovle new ones when possible
  - Pay special attention to corner cases/operations: first node, last digit of binary add, ...

### Classic List

  - 207 Course Schedule
    - Graph, DFS to detect circle
  - 240 Search a 2D Matrix II: 2-D binary search
  - 264 Ugly Number II
  - 322 Coin Change
    - BFS top down with table buildup
    - BFS bottom up with table buildup
    - BFS top down + bottom up with table buildup
    - Dynamic programming
  - 337 House Robber III
    - Optimal problem + recursive subproblem
    - Dynamic programming
  - 394 Decode String
    - Use Stack
    - Use recursion
  - 416 Partition Equal Subset Sum
    - Recursive
    - DFS with memory
    - Dynamic Programming
  - 647 Palindromic Substrings
    - Dynamic programming
  - 560 Subarray Sum Equals K
    - Intuition, O(n^2), TLE
    - Key is continuous. Get SumSoFar, then Two sum problem. 
    - Be careful about cases ([1, -1, 1, -1], 0). It's counted as 4 cases not 3. 
  - 236 Lowest Common Ancestor of a Binary Tree
    - Recursion
    - DFS + stack + dictionary 
    - DFS + recursion + backtrack 
  - 295 Find Median from Data Stream
    - Need to memorize all the incoming data
    - Use two heap to store small and large half
  - 239 Sliding Window Maximum
  
### Binary, Int

Use **bin(num)**, **int(str, 2)**

```python
 a = '0b111'
 # Convert to int
 int(a,2)

 a =7
 # convert to binary
 bin(a)
```

### Dynamic Programming

Key Points:
  - Any problem that can get solved by using smaller solved sub-problems
  - Identity sub-problems and Use solved sub-problems for larger problem
  - Sub-problems on Sub-problems on Sub-problems

Dynamic programming amounts to breaking down an [optimization] problem into simpler sub-problems, and storing the solution to each sub-problem so that each sub-problem is only solved once. [Here is a good explanation about Dynamic Programming.](https://medium.freecodecamp.org/demystifying-dynamic-programming-3efafb8d4296)

DP is a useful technique for optimization problems, those problems that seek the maximum or minimum solution given certain constraints, because it looks through all possible sub-problems and never recomputes the solution to any sub-problem. 

Sub-problems are smaller versions of the original problem. In fact, sub-problems often look like a reworded version of the original problem. If formulated correctly, sub-problems build on each other in order to obtain the solution to the original problem.
  
There are three ways to do Dynamic Programming: 
  - Backtracking: recursively solving the problem
  - Top-down dynamic programming: build a memoization table to reduce computation, a way to optimize backtracking.
  - Bottom-up dynamic programming: top-down to bottom-up conversion is done by eliminating recursion.
  - A good example: https://leetcode.com/articles/jump-game/

Example problems:
  - 62 Unique Paths
  - 91 Decode Ways
  - 44 Wildcard Matching: recursion -> build table -> DP
  - 300 Longest Increasing Subsequence
  - 309 Best Time to Buy and Sell Stock with Cooldown
  - 416 Partition Equal Subset Sum
  - 338 Counting Bits
  - 329 Longest Increasing Path in a Matrix
### DFS

Trick:
  - DFS and pass down parameters

### BFS
  
Example Problems:
  - 79 Word Search
  - 322 Coin Change
    - BFS top down
    - BFS bottom up with table buildup
  - 279 Perfect Squares
  - 236 Lowest Common Ancestor of a Binary Tree
  
### Greedy

  - Problems can be solved like maxReach = max(maxReach, i+x), where i+x is current reach.
  
Example problems:
  - 55 Jump Game
  - 45 Jump Game II

### Recursive

Example problems:
  - 40 Combination Sum II
  - 139 Word Break: recursion -> build table
  - 416 Partition Equal Subset Sum
  - 236 Lowest Common Ancestor of a Binary Tree
  
### Divide And Conquer

Example problems:
  - 131 Palindrome Partitioning
  
### Backtrack

Example problems:

### Linked List

  - Remember to work through one or two test cases, easy to miss/mess some pointer things.
  - It's all about rearrange connections.
  - Remember to use Dummy Head Node to make life easier.
  - Use points for many problems: two, three or four.
  - Careful about issue related to first node.
  - Careful about the nodes connection change. 
  - Partition List: separate one list into two lists and then combine together. Example: 86 Partition List

### Array/List problems

Trick
  - One, Two pointers
  - One or Two extra help arrays/lists: Trapping Rain Water, Product of Array Except Self 
  - From two ends and approaching middle
  - Use dictionary to save some results, similar to saving the solved results in dynamic programming 
  - Travel the list twice, once for processing to get some info, second time to find the answer.  
  
### Binary Tree Traversal

Problems uses in-order, pre-order, post-order traversal or level order travesal:
  - 129 Sum Root to Leaf Numbers: post-order traversal with additional flag.

### Graph Problems

Classis Problems:
  - 207 Course Schedule  

### Tricky Math/Algorithm

Example problems:
  - 134 Gas Station
  - 201 Bitwise AND of Numbers Range, liked this algorithm.
  - 213 House Robber II
  - 220 Contains Duplicate III
  - 287 Find the Duplicate Number
  - 165 Compare Version Numbers: be extremely careful about different cases
  - 406 Queue Reconstruction by Height
    - Sort first
    - Sort height ascending and count descending
    - Start from end
