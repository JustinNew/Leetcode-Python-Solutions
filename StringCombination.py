# Using Recursive Method.
# n, number of characters
# r, number of characters to pick
# idx, index of pick from n characters
# k, number of characters picked

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        import operator
        import functools

        times = []
        arr = [1,2,4,8,16,32,100,200,400,800]
        if num==0:
            times.append(str('0:00'))
            return times
        else:
            result = self.StringCombination(arr, num)

        for i in result:
            sum = functools.reduce(operator.add, i)
            hour = int(sum/100)
            min = sum%100
            if hour>11 or min>59:
                next
            elif min<10:
                times.append(str(hour)+':0'+str(min))
            else:
                times.append(str(hour)+':'+str(min))
        return times

    def StringCombination(self, arr, num):
        # arr is the string/array
        # num is the number of characters to pick 

        res_t = [0 for i in range(num)]
        res = []

        if num==0:
            return
        elif num>len(arr):
            return
        else:
            self.utilCombination(arr, 0, len(arr), 0, num, res_t, res)    
            return res

    def utilCombination(self, arr, idx, n, k, r, res_t, res):

        if k==r:
           res.append(list(res_t))
           return

        for i in range(idx, n):
            res_t[k] = arr[i]
            self.utilCombination(arr, i+1, n, k+1, r, res_t, res)

        return

if __name__=='__main__':

    so = Solution()
    print (so.readBinaryWatch(2)) 
