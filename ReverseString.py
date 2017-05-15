# Reverse a string input.

def ReverseString(s):
    new = ''   

    i = len(s)-1
    while i >=0:
        new = new + s[i]
        i -= 1

    return new

def Reverse(s):
    return s[::-1]

class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])


class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]

if __name__ == '__main__':
     s = 'I am a cool kid.'
     print 'Method 1: %s' %ReverseString(s)
     print 'Method 2: %s'%Reverse(s)
