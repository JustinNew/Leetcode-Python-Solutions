class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = list()
        new = sorted(nums)

        i = 0
        j = len(new) - 1

        while i < j:
            if new[i] + new[j] < target:
                i += 1
            elif new[i] + new[j] > target:
                j -= 1
            else:
                one = new[i]
                two = new[j]

        if i < j:
            for k in range(len(nums)):
                if one == nums[k] or two == nums[k]:
                    result.append(k)
            
        return sorted(result)

    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i
            else:
                return map[num[i]], i

        return -1, -1
