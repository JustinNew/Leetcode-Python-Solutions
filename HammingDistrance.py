# Find the hamming distance for two integers.

def HamDist(a,b):
    return bin(a^b).count('1')

if __name__=='__main__':
    a = 8
    b = 2
    sum = HamDist(a, b)
    print 'The Hamming Distance for %d and %d is %d.'%(a,b,sum)
