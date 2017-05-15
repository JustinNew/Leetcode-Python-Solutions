class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return '0'
        elif num < 0:
            num = -num - 1
            num = num^0xffffffff

        s = ''
        while num>0:
            left = num%16
            num = num//16
            if left == 10:
                s = s + 'a'
            elif left == 11:
                s = s + 'b'
            elif left == 12:
                s = s + 'c'
            elif left == 13:
                s = s + 'd'
            elif left == 14:
                s = s + 'e'
            elif left == 15:
                s = s + 'f'
            else:
                s = s + str(left)

        return s[::-1]

if __name__=='__main__':

     a = -1
     so = Solution()

     print(so.toHex(a))
