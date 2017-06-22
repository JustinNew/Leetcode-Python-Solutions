# Given a list of array, return a list of arrays, each array is a combination of one element in each given array.
# Suppose the input is [[1, 2, 3], [4], [5, 6]], the output should be [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]].

def PermArrayOfArrays(nums):

    result = []
    temp = []

    util(nums, 0, temp, result)

    return result

def util(nums, i, temp, result):

    if i == len(nums):
        result.append(temp)
        return

    for j in nums[i]:
        util(nums, i+1, temp+[j], result) 

if __name__=='__main__':

    a = [[1, 2, 3], [4], [5, 6]]

    print (PermArrayOfArrays(a))
