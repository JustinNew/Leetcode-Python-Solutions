# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.

def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n


def firstMissingPositive(self, A):
    n = len(A)

    # Move n to the (n-1)th place until no move can be made.
    for index in xrange(n):
        element = A[index]
        while True:
            if element <= 0 or element > n or element == A[element - 1]:
                break
            A[element - 1], element = element, A[element - 1]

    for index in xrange(n):
        if A[index] != index + 1:
            return index + 1

    return n + 1
