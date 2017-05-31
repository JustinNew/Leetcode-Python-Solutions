class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
            
        result = [[]]
        nums = sorted(nums)
        l_l = []
        
        last = float('nan')
        for i in nums:
            temp = []
            
            if i != last:
                last = i
                for j in result:
                    temp.append(j+[i])
            else:
                for j in l_l:
                    temp.append(j+[i])
                    
            l_l = [k for k in temp]
            result += temp
            
        return result
