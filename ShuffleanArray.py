# 384. Shuffle an Array

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.org = [i for i in nums]

        return 

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        
        return self.org

    # Get all the possible permutation is too much.
    # Time Limit Exceeded.

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import numpy as np
        if len(self.arr) == 0:
            return []
        
        result = [[self.arr[0]]]
        for i in range(1, len(self.arr)):
            temp = []
            for l in result:
                for j in range(len(l) + 1):
                    tt = [k for k in l]
                    tt.insert(j, self.arr[i])
                    temp.append(tt)
            result = temp

        return result[np.random.randint(0, len(result))]

    def shuffle2(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from numpy.random import randint
        result = []
        while len(self.arr) != 0:
            i = randint(0, len(self.arr))
            result.append(self.arr.pop(i))
            
        self.arr = [i for i in self.org]
        return result

    # Permuation is actually swapping.
    def shuffle3(self):
        import random

        ans = self.arr[:]                     # copy list
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index 
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == '__main__':

    so = Solution([1,2,3,4,5,6,7,8,9,10,11,12])
    print(so.shuffle3())
    print(so.reset())
    for i in range(10):
        print(so.shuffle3())
