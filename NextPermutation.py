# 31. Next Permutation
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# Steps:
# 1. Exchange: whether we can make change for the -2 position to make it bigger; 
#              whether we can make change for the -3 position to make it bigger;
#              ... 
# 2. Rearrange: rearrange the digits between (ToExchange-1) and -1 so that it is the smallest possible.
# Be very careful about the bubble sort index.

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # Exchange
        flag = 0
        ToExchange = -1
        Exchange = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                ToExchange = i
                break;

        if ToExchange != -1:
            for i in range(len(nums)-1, ToExchange, -1):
                if nums[i] > nums[ToExchange]:
                    if Exchange == -1:
                        Exchange = i
                    elif nums[Exchange] > nums[i]:
                        Exchange = i        

        position = ToExchange
        if Exchange != ToExchange:
            nums[Exchange], nums[ToExchange] = nums[ToExchange], nums[Exchange] 
            flag = 1

        # Rearrange
        if flag == 1:
            for i in range(len(nums) - position - 1):
                for m in range(position+1, len(nums) - 1 - i):
                    if nums[m] > nums[m+1]:
                        nums[m], nums[m+1] = nums[m+1], nums[m]
        else:
            nums.sort()

        print (nums)
        return
        
class Solution2:

    def nextPermutation(self, l):

        # Find the first ToExchange.
        flag = 0
        for i in range(len(l) - 2, -1, -1):
            ToExchange = i

            for j in range(i+1, len(l)):
                if l[j] > l[i]:
                    flag = 1
                    Exchange = j
                    break

            if flag == 1:
                break

        if flag == 0:
            l = l[::-1]
            print (l)
            return

        # Check to get the min() that is larger than l[ToExchange]
        for i in range(ToExchange + 1, len(l)):
                if l[i] > l[ToExchange]:
                    if l[i] < l[Exchange]:
                        Exchange = i

        # Exchange
        l[ToExchange], l[Exchange] = l[Exchange], l[ToExchange]

        # Rearrange to get the minimum.
        l = self.rearrange(l, ToExchange+1, len(l) - 1)

        print (l)
        return 

    def rearrange(self, l, i, j):

        for m in range(j - i):
            for n in range(i, len(l) - m - 1):
                if l[n] > l[n+1]:
                    l[n], l[n+1] = l[n+1], l[n]

        return l

if __name__ == '__main__':

    s = Solution2()
    s.nextPermutation([1,2,3])
