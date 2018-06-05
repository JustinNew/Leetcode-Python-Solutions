# 264. Ugly Number II

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        step =  2
        result = []
        result.append(1)
        count = 1
        while True:
            if count == n:
                return result[-1]

            if self.util(step):
                result.append(step)
                count += 1

            step += 1

    def util(self, x):

        while x % 2 == 0:
            x = x / 2

        while x % 3 == 0:
            x = x / 3

        while x % 5 == 0:
            x = x / 5

        if x == 1:
            return True
        else:
            return False

if __name__ == '__main__':

    so = Solution()
    print(so.nthUglyNumber(259))

'''
This generates the first n ugly numbers, in order from smallest to largest, in O(n) time. 
For each prime 2, 3 and 5, have an index to the next number that can be multiplied with the prime to produce a new ugly number. 
Update the three indexes and then add the smallest of the three candidate ugly numbers.

1. Use the existing ugly number to generate new ones by multiply 2, 3 or 5.
2. There are three lines of candidates, one for 2, one for 3 and the last for 5.
3. Always pick the smallest one and update the candidates. 
'''

def nthUglyNumber(n):
    ugly = [1]

    # Use the first ugly number to generate the next possible.
    i2 = i3 = i5 = 0

    while len(ugly) < n:
        # Use existing ugly numbers to generate new ones by multiply 2 until a new large enough one is generated.
        while ugly[i2] * 2 <= ugly[-1]: i2 += 1
 
        # Another candidate. 
        # i3 is another line of queue.
        while ugly[i3] * 3 <= ugly[-1]: i3 += 1

        # The third candidate:
        while ugly[i5] * 5 <= ugly[-1]: i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))

    return ugly[-1]

print(nthUglyNumber(259))
