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
  - 240 Search a 2D Matrix II: 2-D binary search
  - 264 Ugly Number II
  
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

  - Problems can be solved like F(n) = F(n-1) + F(n-2)
  
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
 
### DFS

Trick:
  - DFS and pass down parameters

### BFS
  
Example Problems:
  - 279 Perfect Squares

Example problems:
  - 79 Word Search
  
### Greedy

  - Problems can be solved like maxReach = max(maxReach, i+x), where i+x is current reach.
  
Example problems:
  - 55 Jump Game
  - 45 Jump Game II

### Recursive

Example problems:
  - 40 Combination Sum II
  - 139 Word Break: recursion -> build table
  
### Divide And Conquer

Example problems:
  - 131 Palindrome Partitioning
  
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
  
### Special Cases

#### Tricky Math/Algorithm

Example problems:
  - 134 Gas Station
  - 201 Bitwise AND of Numbers Range, liked this algorithm.
  - 213 House Robber II
  - 220 Contains Duplicate III
  - 287 Find the Duplicate Number
  
#### Need Be Carefull

Example problems:
  - 165 Compare Version Numbers

## Algorithms

#### 236 Lowest Common Ancestor of a Binary Tree

#### Reservoir Sampling

```sh
Init : a reservoir with the size： k  
  
for i= k+1 to N  
  
    M=random(1, i);  
  
    if( M < k)  
  
     SWAP the Mth value and ith value  
  
end for
```

#### Find Median from Data Stream

#### Permuation without recursion
The basic idea is, to permute n numbers, we can add the nth number into the resulting List<List<Integer>> from the n-1 numbers, in every possible position.

Get permutation of [1,2,3]
  - [[1]]
  - [[2,1], [1,2]]
  - [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2],[1,2,3]]


#### Symmetric Tree

Solve it recursively.
  - root.left isMirror root.right
  - left.left isMirror right.right and left.right isMirror right.left
  
#### String permutation
    
Solve it recursively:
  - Try all n characters in the first position and reduce it to a n-1 characters permutation, ...
  - Combination is using two pointers.
  - Permutation is using one pointer.
  
Example Problems:
  - 634 Find the Derangement of An Array
  
#### Intersection of Two Linked Lists
    
At least three ways: 
  - Make a cycle in the list and find the cycle start
  - L1 + L2 and L2 + L1 should have the same ending
  - Let two pointers start from the places having the same distance from their end

#### Is Linked List Palidrome 
        
Reverse the second half of the linked list.

Note: 
  - Do change to part of the data.
