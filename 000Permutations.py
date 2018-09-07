# 46. Permutations

# Be careful about list append and mutation at the same time.
# Need to create a new list instead of using the mutated list itself.

class Solution:
    # Create a new list when go further.
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def helper(arr, i):
            if i == len(arr):
                result.append(arr)
                return

            for j in range(i, len(arr)):
                temp = [k for k in arr]
                temp[i], temp[j] = temp[j], temp[i]
                helper(temp, i + 1)

            return

        helper(nums, 0)
        return result

    # When append to result, do not append arr directly.
    # Need to do backtrack.
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def helper(arr, i):
            if i == len(arr):
                result.append([k for k in arr])
                return
            
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                helper(arr, i + 1)
                arr[i], arr[j] = arr[j], arr[i]
            
            return
            
        helper(nums, 0)
        return result
            

########################################################
# Excellent solution.
# Without recursion
# The basic idea is, to permute n numbers, we can add the nth number into 
# the resulting List<List<Integer>> from the n-1 numbers, in every possible position.
# 1. [[1]]
# 2. [[2,1], [1,2]]
# 3. [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2],[1,2,3]]
#

def permute(self, nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   # Insert n
        perms = new_perms
    return perms


# 47. Permutations II

class Solution:

    # To handle duplication, just avoid inserting a number after any of its duplicates.
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = [[]]
        for i in nums:
            temp = []
            for l in result:
                for j in range(len(l) + 1):
                    temp.append(l[:j] + [i] + l[j:])
                    if j < len(l) and i == l[j]:   # Handle duplicates, very tricky 
                        break
            result = temp

        return result
