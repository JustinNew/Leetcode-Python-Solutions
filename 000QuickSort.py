# Quick Sort

def quickSort(nums):

    if len(nums) <= 1:
        return nums

    small = []
    equal = []
    large = []

    for i in range(0, len(nums)):
        if nums[i] == nums[0]:
            equal.append(nums[i])
        elif nums[i] < nums[0]:
            small.append(nums[i])
        else:
            large.append(nums[i])

    return quickSort(small) + equal + quickSort(large)

print(quickSort([1,6,2,4,8,3,1,4,12,19,21,11,9,8]))
