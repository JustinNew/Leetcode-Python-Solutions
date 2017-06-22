# Example:
#     include A and do the following
#     and, not include A and do the following

# Recursively.

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        
        self.util(0, len(nums)-1, nums, result, temp)
        
        return result
        
    def util(self, start, end, nums, result, temp):
        
        if start > end:
            result.append(temp)
            return

        self.util(start+1, end, nums, result, temp)
        self.util(start+1, end, nums, result, temp+[nums[start]])
        
        return

if __name__=='__main__':

    a = [1,2,3]
    so = Solution()

    print (so.subsets(a))


#
# Thinking from the existing lists.
#

# Iteratively.

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
    	if S == []:
    		return []
        S.sort() #sort the array to avoid descending list of int
        res=[[]]
        for element in S:
        	temp = []
        	for ans in res:
        		 #append the new int to each existing list
        		temp.append(ans+[element])
        	res += temp
        return res


# With duplicates in the array items.
# For duplicated items, just add to the items in the last round instead of all in the result.

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
