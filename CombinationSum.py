class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []
        temp = []
        candidates.sort()

        self.util(candidates, target, 0, result, temp)

        return result

    def util(self, nums, target, index, result, temp):

        if target == 0:
            if len(temp) != 0:
                result.append(temp)
                return
        elif target < 0:
            return

        for i in range(index, len(nums)):
            self.util(nums, target - nums[i], i, result, temp+[nums[i]])

    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        stack = [(0, 0, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target:
                result.append(res)
            for n in range(start, len(candidates)):
                t = total + candidates[n]
                if t > target:
                    break
                stack.append((t, n, res + [candidates[n]]))
        return result



if __name__=='__main__':

    so = Solution()
    print (so.combinationSum([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73], 310))
