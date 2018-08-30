# 40. Combination Sum II
# Solve the problem recursively.
# Trick: how to avoid duplicated combinations.

class Solution(object):

    ######################################################################################################
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        temp = []
        candidates.sort(reverse=True)

        self.util(candidates, target, result, temp)
        return result       

    def util(self, nums, target, result, temp):

        for i in range(len(nums)): 
            if nums[i] == target and (temp + [nums[i]] not in result):
                result.append(temp + [nums[i]])
            elif nums[i] < target:
                self.util(nums[i + 1:], target - nums[i], result, temp + [nums[i]])

        return

######################################################################################################
def combinationSum2(self, candidates, target):
    # Sorting is really helpful, se we can avoid over counting easily
    candidates.sort()                      
    result = []
    self.combine_sum_2(candidates, 0, [], result, target)
    return result
    
def combine_sum_2(self, nums, start, path, result, target):
    # Base case: if the sum of the path satisfies the target, we will consider 
    # it as a solution, and stop there
    if not target:
        result.append(path)
        return
    
    for i in xrange(start, len(nums)):
        # Very important here! We don't use `i > 0` because we always want 
        # to count the first element in this recursive step even if it is the same 
        # as one before. To avoid overcounting, we just ignore the duplicates
        # after the first element.
        if i > start and nums[i] == nums[i - 1]:
            continue

        # If the current element is bigger than the assigned target, there is 
        # no need to keep searching, since all the numbers are positive
        if nums[i] > target:
            break

        # We change the start to `i + 1` because one element only could
        # be used once
        self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                           result, target - nums[i])

    return  

    ################################################################################################
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) < target:
            return []
        if min(candidates) > target:
            return []    
    
        result = [[]]
        candidates.sort()
        for i in range(len(candidates)):
            # Deal with duplicates
            if i - 1 >= 0 and candidates[i] == candidates[i - 1]:
                t = []
                for l in temp:
                    t.append(l + [candidates[i]])
                temp = t
            else:
                temp = []
                for l in result:
                    temp.append(l + [candidates[i]])
                temp = [l for l in temp if sum(l) <= target]
                # Early stop to deal with Time Limit Exceeded.
                if len(temp) == 0:
                    break
                                  
            result += temp
  
        return [l for l in result if sum(l) == target]
